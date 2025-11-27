from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rapidfuzz import fuzz
import nltk

nltk.download('punkt')
nltk.download('stopwords')

SYMPTOM_KEYWORDS = [
    "fever", "cough", "cold", "headache", "vomiting", "pain",
    "diarrhea", "throat", "heart pain", "chest pain", "fatigue", "nausea"
]

def extract_entities(text: str):
    words = word_tokenize(text.lower())
    filtered = [word for word in words if word.isalpha() and word not in stopwords.words('english')]
    
    found = set()
    for word in filtered:
        for keyword in SYMPTOM_KEYWORDS:
            if fuzz.partial_ratio(word, keyword) > 80:
                found.add(keyword)
    
    for phrase in SYMPTOM_KEYWORDS:
        if fuzz.partial_ratio(phrase, text.lower()) > 80:
            found.add(phrase)
    
    return {"symptoms": list(found)}
# Utility functions to handle other chatbot-related tasks, if needed

def preprocess_input(user_input):
    # Example preprocessing function
    return user_input.strip().lower()

def postprocess_response(response):
    # Example postprocessing function
    return response.strip()
