
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%Sp on %B %d, %Y"),
        'hostname': socket.gethostname()''
        'message': 'You are doing greate, human!! <3',
        'deployed_on': 'kubernetes'
    })

@app.route('/')
def home():
    return "Python App is Running"

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status':'up'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
