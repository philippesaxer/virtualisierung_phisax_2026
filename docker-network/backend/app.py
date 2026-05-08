from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        service="backend",
        hostname=socket.gethostname(),
        remote_addr=request.remote_addr
    )

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)