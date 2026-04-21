from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "watch-protocol backend running"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/test")
def test():
    return jsonify({
        "status": "ok",
        "environment": os.environ.get("ENVIRONMENT", "production"),
        "python_version": "3.12"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
