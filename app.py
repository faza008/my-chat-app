from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/avatars/<filename>')
def get_avatar(filename):
    return send_from_directory('static/avatars', filename)

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

@socketio.on('reaction')
def handle_reaction(data):
    emit('reaction', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
