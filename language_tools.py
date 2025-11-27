# utils/language_tools.py

def translate_to_english(text):
    # Import here to avoid circular import issues
    from utils.response_generator import generate_response
    # Placeholder for actual translation logic (you can integrate APIs like Google Translate)
    return text

def detect_symptom(text):
    # Placeholder function for detecting symptoms
    symptoms = ["fever", "cough", "headache", "chest pain"]
    detected_symptoms = []
    for symptom in symptoms:
        if symptom in text.lower():
            detected_symptoms.append(symptom)
    return detected_symptoms
