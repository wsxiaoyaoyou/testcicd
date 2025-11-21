from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/ping")
def ping():
    return jsonify(ping="pong")

from flask import send_from_directory
@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

app.run(host="0.0.0.0", port=5000)