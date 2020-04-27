import io from 'socket.io-client';
import * as handler from './index.js';

const roomName = window.location.href.substr(window.location.href.lastIndexOf('/') + 1);
var socket = io('http://localhost:5005',{
    transports: ['websocket'],
    upgrade: false
});

socket.on('message', function(data) {
    console.log(data);
})

socket.on('connected', function(data) {
    console.log('socket connected~~~~');
})

socket.on('session_confirm', function(remoteId) {
  console.log('session_confirm: session_id:${remoteId}');
})

socket.on('bot_uttered', function(data) {
    console.log('New message from backend: ', data);
    if (data.user_utterance) {
      handler.addUserMessage(data);
    }
    handler.receivedBotMessage(data);
})

export function sendUserMessage(msg) {
    socket.emit('user_uttered',{'message':msg});
}
