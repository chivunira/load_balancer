import requests
from flask import Flask, request, jsonify
import random
import logging
import os

app = Flask(__name__)

# List to store server replicas
server_replicas = ["http://localhost:5001", "http://localhost:5002", "http://localhost:5003"]

# Ensure the logs directory exists
log_dir = '/app/logs'
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logging.basicConfig(filename=os.path.join(log_dir, 'server_selection.log'), level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to get status of server replicas
def get_server_replicas():
    return {'N': len(server_replicas), 'replicas': server_replicas}

# Function to route requests to server replicas
def route_request():
    global server_replicas
    if not server_replicas:
        return "Error: No server replicas available"

    # Simple round-robin load balancing
    return random.choice(server_replicas)

# Endpoint for /rep
@app.route('/rep', methods=['GET'])
def get_replicas():
    replicas_status = get_server_replicas()
    return jsonify(replicas_status)

# Endpoint for /add
@app.route('/add', methods=['POST'])
def add_servers():
    data = request.get_json()
    num_instances = data.get('n')
    hostnames = data.get('hostnames')

    if hostnames and len(hostnames) != num_instances:
        return jsonify(
            {'message': 'Error: Number of hostnames does not match the number of instances', 'status': 'error'}), 400

    if hostnames:
        server_replicas.extend(hostnames)
    else:
        for i in range(num_instances):
            server_replicas.append(f"http://localhost:{len(server_replicas) + 5001}")

    return jsonify({'message': {'N': len(server_replicas), 'replicas': server_replicas}, 'status': 'successful'}), 200

# Endpoint for /rm
@app.route('/rm', methods=['DELETE'])
def remove_servers():
    data = request.get_json()
    num_instances = data.get('n')
    hostnames = data.get('hostnames')

    if hostnames:
        num_hostnames = len(hostnames)

        if num_hostnames > num_instances:
            return jsonify({'message': 'Error: Number of hostnames exceeds the specified number of instances to remove',
                            'status': 'error'}), 400

        num_additional_instances = num_instances - num_hostnames
        additional_hostnames = random.sample(server_replicas, num_additional_instances)
        hostnames_to_remove = hostnames + additional_hostnames

        if num_hostnames < num_instances:
            random_instance_to_remove = random.choice(hostnames_to_remove)
            hostnames_to_remove.remove(random_instance_to_remove)

        for hostname in hostnames_to_remove:
            if hostname in server_replicas:
                server_replicas.remove(hostname)
    else:
        for _ in range(num_instances):
            if server_replicas:
                server_replicas.pop()

    return jsonify({'message': {'N': len(server_replicas), 'replicas': server_replicas}, 'status': 'successful'}), 200

# Endpoint for /
@app.route('/', methods=['GET'])
def route_request_to_server():
    server = route_request()
    if server:
        logging.info(f"Request redirected to server: {server}")
        return f"Request routed to server: {server}", 200
    else:
        return "Error: No server replicas available", 400

@app.route('/home', methods=['GET'])
def route_home_request_to_server():
    server = route_request()
    print("Selected Server:", server)
    if server:
        try:
            response = requests.get(f"{server}/home")
            if response.status_code == 200:
                logging.info(f"Request redirected to server: {server}")
                return f"Request routed to server: {server}\n{response.text}", 200
            else:
                return f"Error: {response.status_code}", response.status_code
        except Exception as e:
            logging.error(f"Request to {server} failed with error: {str(e)}")
            return f"Error: {str(e)}", 500
    else:
        return "Error: No server replicas available", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
