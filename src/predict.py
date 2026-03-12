import pickle

# Load model
with open("models/chat_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_intent(user_input):
    
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]

    return prediction