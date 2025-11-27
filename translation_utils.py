from transformers import pipeline
from langdetect import detect

# Load translation models
en_to_hi = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
hi_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")
en_to_mr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-mr")
mr_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-mr-en")

def detect_language(text: str) -> str:
    """Detect language of the input text."""
    try:
        lang = detect(text)
        if lang in ["hi", "mr", "en"]:
            return lang
    except:
        pass
    return "en"

def translate_to_english(text: str) -> str:
    """Translate text to English."""
    lang = detect_language(text)
    if lang == "hi":
        return hi_to_en(text)[0]['translation_text']
    elif lang == "mr":
        return mr_to_en(text)[0]['translation_text']
    else:
        return text

def translate_from_english(text: str, target_lang: str) -> str:
    """Translate text from English to a target language."""
    if target_lang == "hi":
        return en_to_hi(text)[0]['translation_text']
    elif target_lang == "mr":
        return en_to_mr(text)[0]['translation_text']
    else:
        return text
