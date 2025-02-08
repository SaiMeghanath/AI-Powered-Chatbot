import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Download necessary NLTK data
nltk.download("punkt")

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

# Improved text preprocessing
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())  # Tokenize and lowercase
    return " ".join(tokens)  # Convert back to a string

# Convert text data into numerical data
vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words="english")
classifier = MultinomialNB()

# Train the model
X = vectorizer.fit_transform(patterns)
y = np.array(tags)
classifier.fit(X, y)

# Chatbot function
def chatbot_response(user_input):
    user_input = [preprocess(user_input)]  # Preprocess input
    X_input = vectorizer.transform(user_input)
    tag = classifier.predict(X_input)[0]  # Predict intent
    return random.choice(responses[tag])  # Pick a random response from that intent

# Run the chatbot
print("AI Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("AI Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("AI Chatbot:", response)
