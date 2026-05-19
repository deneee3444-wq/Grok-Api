from flask import Flask, request, jsonify
from core import Grok

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "çalışıyor"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data.get("message")
    model = data.get("model", "grok-3-fast")
    extra_data = data.get("extra_data", None)

    if not message:
        return jsonify({"error": "message zorunlu"}), 400

    try:
        response = Grok(model).start_convo(message, extra_data=extra_data)
        return jsonify({
            "response": response["response"],
            "extra_data": response["extra_data"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
