from flask import Flask, request, jsonify
import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download("punkt")

app = Flask(__name__)

# Load intents from JSON file
with open("intents.json", "r") as file:
    data = json.load(file)

# Prepare training data
patterns = []
tags = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Preprocess text
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())  # Tokenize and lowercase
    return " ".join(tokens)  # Convert back to a string

# Train the model
vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words="english")
classifier = MultinomialNB()
X = vectorizer.fit_transform(patterns)
y = np.array(tags)
classifier.fit(X, y)

# API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "Please provide a message."})
    
    processed_input = preprocess(user_input)
    X_input = vectorizer.transform([processed_input])
    tag = classifier.predict(X_input)[0]
    response = random.choice(responses[tag])

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
