import streamlit as st
import random
from src.predict import predict_intent
from src.utils import load_intents

# Load intents
intents = load_intents()

# Get response
def get_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Streamlit UI
st.title("🌍 AI Travel Assistant")
st.write("Ask me about flights, hotels, travel plans ✈️")

user_input = st.text_input("Type your message")

if st.button("Send"):

    if user_input:
        tag = predict_intent(user_input)
        response = get_response(tag)

        st.write("🤖 Bot:", response)