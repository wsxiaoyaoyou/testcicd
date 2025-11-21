from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='/')

# ---------- API ----------
@app.route("/api/ping")
def ping():
    return jsonify(ping="hello")

# ---------- 前端 ----------
@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

# 404 也返回 index.html，让 Vue Router 接管
@app.errorhandler(404)
def fallback(e):
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)