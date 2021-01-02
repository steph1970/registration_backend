from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
import time

REGISTRATION_SERVICE_HOST='localhost'
REGISTRATION_SERVICE_PORT='5001'

REGISTRATION_SERVICE_URL = 'http://%s:%s' % (REGISTRATION_SERVICE_HOST, REGISTRATION_SERVICE_PORT)
DASHBOARD_URL = '%s/dashboard' % REGISTRATION_SERVICE_URL
SUBMISSIONS_URL = '%s/submissions' % REGISTRATION_SERVICE_URL

app = Flask(__name__)
socketio = SocketIO(app, logger=True)

@app.route('/')
def hello_world():
    return 'Hello world !'

@app.route('/submissions', methods=['GET'])
def get_submissions():
    response = requests.get(SUBMISSIONS_URL)
    json_subms = response.json()
    return render_template('submissions_list.html', submissions=json_subms.get("Submissions"))

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5002)