from transformers import pipeline

# Load the NER model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_intent(text: str):
    # Extract named entities
    entities = ner_pipeline(text)
    
    # Filter out entities related to medical intents
    medical_entities = [entity['word'] for entity in entities if 'disease' in entity['entity']]
    
    return medical_entities
