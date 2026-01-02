from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string

# Predefined Q&A
qa_pairs = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a nice day!",
    "how are you": "I am fine 🙂. How about you?",
    "what is python": "Python is a popular programming language used for web, AI, and more.",
    "what is flask": "Flask is a lightweight Python web framework used to build web apps.",
    "who are you": "I am an AI Chatbot created to answer your questions.",
    "help": "You can ask me about Python, Flask, greetings, or just say hi!"
}

# Prepare corpus
questions = list(qa_pairs.keys())
answers = list(qa_pairs.values())

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer().fit(questions)

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def get_response(user_input):
    user_input_clean = clean_text(user_input)
    # Vectorize input
    input_vec = vectorizer.transform([user_input_clean])
    question_vecs = vectorizer.transform(questions)
    # Cosine similarity
    sim_scores = cosine_similarity(input_vec, question_vecs)
    # Best match
    best_idx = np.argmax(sim_scores)
    if sim_scores[0][best_idx] > 0.1:
        return answers[best_idx]
    else:
        return "Sorry, I didn't understand. Can you rephrase?"
