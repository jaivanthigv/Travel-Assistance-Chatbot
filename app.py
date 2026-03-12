import random
from src.predict import predict_intent
from src.utils import load_intents

# Load intents
intents = load_intents()

def get_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."

def run_chatbot():

    print("🌍 Travel Assistant Chatbot")
    print("Type 'quit' to exit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Bot: Goodbye! Safe travels ✈️")
            break

        tag = predict_intent(user_input)

        response = get_response(tag)

        print("Bot:", response)


if __name__ == "__main__":
    run_chatbot()