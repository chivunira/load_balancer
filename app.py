from flask import Flask
import os

app = Flask(__name__)

@app.route('/home')
def home():
    server_id = os.environ.get('SERVER_ID', 'Unknown')
    return f"Hello from Server: {server_id}"

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '', 200

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)