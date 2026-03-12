import json
import pickle

# Load intents dataset
def load_intents():
    with open("data/intents.json", "r") as file:
        intents = json.load(file)
    return intents


# Load trained ML model
def load_model():
    with open("models/chat_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


# Load vectorizer
def load_vectorizer():
    with open("models/vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)
    return vectorizer