from flask import Flask,render_template
from flask_socketio import SocketIO,emit

app=Flask(__name__)
app.config['SECRET_KEY']="secret"
socketio=SocketIO(app,cors_allowed_origins="*")

@socketio.on('message')
def getmsg(message):
    emit('mymsg',message,broadcast=True)

@app.route('/')
def message():
    return render_template('message.html')

if __name__=='__main__':
    socketio.run(app,debug=True)