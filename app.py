from datetime import datetime, timezone
from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

started_at = datetime.now(timezone.utc)
message_count = 0

messages = [
    {"text": "Hello from the Flask backend!", "tag": "Backend"},
    {"text": "Your app is ready for Docker.", "tag": "Docker"},
    {"text": "Small apps are best for learning DevOps.", "tag": "DevOps"},
    {"text": "Health checks make deployments easier.", "tag": "Monitoring"},
    {"text": "Kubernetes can restart failed containers.", "tag": "Kubernetes"},
    {"text": "AWS EC2 is a good first deployment target.", "tag": "Cloud"},
    {"text": "Ship small, verify often.", "tag": "Practice"},
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/message")
def message():
    global message_count
    message_count += 1
    selected = random.choice(messages)

    return jsonify({
        "message": selected["text"],
        "tag": selected["tag"],
        "count": message_count,
        "served_at": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "webx",
        "uptime_seconds": int((datetime.now(timezone.utc) - started_at).total_seconds()),
    })


@app.route("/stats")
def stats():
    return jsonify({
        "messages_available": len(messages),
        "messages_served": message_count,
        "started_at": started_at.isoformat(),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
