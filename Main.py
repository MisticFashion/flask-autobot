from flask_ngrok import run_with_ngrok
run_with_ngrok(app)  # before app.run()

app = Flask(__name__)

REPLY_MAP = {
    "hi": "👋 Welcome to Mistc! Type:\n1. Night Dress\n2. Period Panty\n3. Bag",
    "1": "🧵 Night Dress Catalog: https://yourlink.com/night",
    "2": "🩲 Period Panty Info: https://yourlink.com/panty",
    "3": "🎒 Bag Collection: https://yourlink.com/bag"
}

@app.route("/", methods=["POST"])    
def auto_reply():
    try:
        data = request.get_json()
        msg = str(data.get("message", "")).strip().lower()
        reply = REPLY_MAP.get(msg, "❓ Sorry, I didn’t understand. Type 'hi' to see menu.")
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

app.run(host="0.0.0.0", port=8080)
