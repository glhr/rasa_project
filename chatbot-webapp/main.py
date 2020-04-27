
import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template

app = Flask(__name__)

rooms = set()
clients = dict()
usermessage = {
        'text': 'Hey this is a dummy user message'
}
botmessage = {
        'text': 'Hey this is a dummy bot message'
}
# usermessages = [usermessage, usermessage, usermessage]
# botmessages = [botmessage, botmessage, botmessage]
usermessages, botmessages = [], []


@app.route("/")
def mainview():
    return render_template("index.html", messages=zip(usermessages, botmessages))


if __name__ == '__main__':
    app.run(port=8080, debug=True, use_reloader=True)
