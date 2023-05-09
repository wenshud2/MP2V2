import subprocess
import socket
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def stress_cpu():
    # Start the stress_cpu.py script as a separate process
    subprocess.Popen(['python', 'stress_cpu.py'])
    return 'Started CPU stress test'


@app.route('/', methods=['GET'])
def get_ip():
    # Get the private IP address of the EC2 instance
    ip_address = socket.gethostname()
    return f'Private IP address: {ip_address}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
