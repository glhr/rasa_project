import logging
import uuid
from sanic import Blueprint, response
from socketio import AsyncServer
from typing import Optional, Text, Any

from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import UserMessage, OutputChannel

import urllib
import time

from speech.utils import get_path_from_filename, get_current_directory

USE_TTS = 'mozilla'
USE_STT = 'google'

logger = logging.getLogger(__name__)

try:
    if USE_TTS == 'pyttsx3':
        from speech import tts_pyttsx3 as tts
    elif USE_TTS == 'mozilla':
        from speech import tts_mozilla as tts
    else:
        USE_TTS = None
except Exception as e:
    logger.warning("Loading TTS module {} failed: {}".format(USE_TTS, e))
    USE_TTS = None

try:
    from speech.stt_wrapper import generate_text
except Exception as e:
    logger.warning("Loading STT module {} failed: {}".format(USE_STT, e))
    USE_STT = None

dirpath = get_current_directory()


class SocketBlueprint(Blueprint):
    def __init__(self, sio: AsyncServer, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(SocketBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options):
        self.sio.attach(app, self.socketio_path)
        super(SocketBlueprint, self).register(app, options)


class SocketIOOutput(OutputChannel):

    @classmethod
    def name(cls):
        return "socketio"

    def __init__(self, sio, sid, bot_message_evt, message):
        self.sio = sio
        self.sid = sid
        self.bot_message_evt = bot_message_evt
        self.message = message

    async def _send_audio_message(self, socket_id, response,  **kwargs: Any):
        # type: (Text, Any) -> None
        """Sends a message to the recipient using the bot event."""

        OUT_FILE = str(time.time())+'.wav'
        OUT_PATH = get_path_from_filename(OUT_FILE)
        tts.generate_speech(response['text'], OUT_PATH)
        link = "http://localhost:8888/"+OUT_FILE

        await self.sio.emit(self.bot_message_evt, {'text': response['text'], 'link': link}, room=socket_id)

    async def send_text_message(self, recipient_id: Text, message: Text, **kwargs: Any) -> None:
        """Send a message through this channel."""

        if USE_TTS:
            await self._send_audio_message(self.sid, {"text": message})
        else:
            await self.sio.emit(self.bot_message_evt, {'text': message, 'link': None}, room=recipient_id)

    async def send_image_url(self, recipient_id: Text, url: Text, **kwargs: Any) -> None:
        bot_message = {
            "attachment": {
                "type": "image",
                "payload": {
                  "title": "image",
                  "src": url
                }
            },
            "link": None
        }
        await self.sio.emit(self.bot_message_evt, bot_message, room=recipient_id)


class SocketIOInput(InputChannel):
    """A socket.io input channel."""

    @classmethod
    def name(cls):
        return "socketio"

    @classmethod
    def from_credentials(cls, credentials):
        credentials = credentials or {}
        return cls(credentials.get("user_message_evt", "user_uttered"),
                   credentials.get("bot_message_evt", "bot_uttered"),
                   credentials.get("namespace"),
                   credentials.get("session_persistence", False),
                   credentials.get("socketio_path", "/socket.io"),
                   )

    def __init__(self,
                 user_message_evt: Text = "user_uttered",
                 bot_message_evt: Text = "bot_uttered",
                 namespace: Optional[Text] = None,
                 session_persistence: bool = False,
                 socketio_path: Optional[Text] = '/socket.io'
                 ):
        self.bot_message_evt = bot_message_evt
        self.session_persistence = session_persistence
        self.user_message_evt = user_message_evt
        self.namespace = namespace
        self.socketio_path = socketio_path

    def blueprint(self, on_new_message):
        sio = AsyncServer(async_mode="sanic", cors_allowed_origins='*')
        socketio_webhook = SocketBlueprint(
            sio, self.socketio_path, "socketio_webhook", __name__
        )

        @socketio_webhook.route("/", methods=['GET'])
        async def health(request):
            return response.json({"status": "ok"})

        @sio.on('connect', namespace=self.namespace)
        async def connect(sid, environ):
            logger.debug("User {} connected to socketIO endpoint.".format(sid))

        @sio.on('disconnect', namespace=self.namespace)
        async def disconnect(sid):
            logger.debug("User {} disconnected from socketIO endpoint."
                         "".format(sid))

        @sio.on('session_request', namespace=self.namespace)
        async def session_request(sid, data):
            if data is None:
                data = {}
            if 'session_id' not in data or data['session_id'] is None:
                data['session_id'] = uuid.uuid4().hex
            await sio.emit("session_confirm", data['session_id'], room=sid)
            logger.debug("User {} connected to socketIO endpoint."
                         "".format(sid))

        @sio.on('user_uttered', namespace=self.namespace)
        async def handle_message(sid, data):

            output_channel = SocketIOOutput(sio, sid, self.bot_message_evt, data['message'])
            if data['message'].startswith("data:audio"):
                try:  # message is an audio file
                    received_file = 'output_'+sid+'.wav'
                    urllib.request.urlretrieve(data['message'], get_path_from_filename(received_file))

                    if USE_STT:
                        message = generate_text(received_file, method=USE_STT)
                    else:
                        message = "Speech to Text isn't available"
                    logger.info('STT ({}): {}'.format(USE_STT, message))
                except Exception as e:  # message is a string
                    logger.error(e)
            else:
                message = data["message"]
                logger.info('TXT: {}'.format(message))

            await sio.emit(self.user_message_evt, {"text": message.casefold()}, room=sid)

            message_rasa = UserMessage(message, output_channel, sid,
                                    input_channel=self.name())
            await on_new_message(message_rasa)

        return socketio_webhook
