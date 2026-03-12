import json
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents dataset
with open("data/intents.json") as file:
    data = json.load(file)

patterns = []
tags = []

# Prepare training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Convert text to vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Train model
model = LogisticRegression()
model.fit(X, tags)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
with open("models/chat_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved in models folder!")