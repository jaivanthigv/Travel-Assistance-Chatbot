from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
model = pickle.load(open("chat_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Predefined intent-based responses
responses = {
    "book_flight": "Sure! I can help you book a flight. Please provide source, destination, and date.",
    "book_hotel": "Got it! Please share location, check-in and check-out dates.",
    "cancel_booking": "Your booking can be cancelled. Please provide booking ID.",
    "faq": "You can check baggage policy, refund details, and more on our website.",
    "greeting": "Hello! How can I assist you with your travel today?",
    "default": "Sorry, I didn’t understand that. Could you rephrase?"
}

# Home route to render HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot responses (JSON input/output)
@app.route("/get", methods=["POST"])
def chatbot_response():
    try:
        data = request.get_json()   # Expecting JSON { "msg": "Hello" }
        user_msg = data.get("msg", "")

        if not user_msg:
            return jsonify({"response": "I didn’t get any message."})

        # Transform user message
        X = vectorizer.transform([user_msg])
        intent = model.predict(X)[0]

        # Get reply from dictionary
        reply = responses.get(intent, responses["default"])

        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
