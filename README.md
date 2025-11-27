

🏥 **Multilingual Healthcare Chatbot**

Supports English, Hindi, Marathi | Translation | Language Detection | Symptom Extraction | GPT-based Response Generation

This project is a multilingual healthcare chatbot designed to assist users with basic health-related queries, symptoms, and general questions. It automatically detects the user's language, translates the input to English for processing, extracts symptoms, and generates accurate responses using a GPT-based model. The chatbot supports English, Hindi, and Marathi.

---

🚀 **Features**

🌐 Multilingual Support

* Supports English, Hindi, Marathi
* Automatic language detection
* Translation to English for processing
* Translation of final response back to user's language

🩺 Symptom Extraction

* NLP-based symptom/entity extraction
* Fuzzy matching with a symptom dictionary
* Handles misspellings and variations

🤖 GPT-based Response Generation

* Integrated GPT-based model (FLAN-T5 / GPT-2 / Custom LLM)
* Handles symptom queries
* Handles general/random questions
* Supports follow-up conversations

🧠 Processing Pipeline
User Input → Language Detection → Translation → Symptom Extraction → GPT Response → Translate Back → Output

💬 Use Cases

* Basic medical guidance
* Symptom checking
* Multilingual patient support
* Healthcare Q&A bot

---

🛠️ **Tech Stack**

| Component           | Technology                                    |
| ------------------- | --------------------------------------------- |
| Language Detection  | langdetect / fasttext                         |
| Translation         | Googletrans / IndicTrans / HuggingFace models |
| Symptom Extraction  | spaCy / FuzzyWuzzy / custom NER               |
| Response Generation | GPT-2 / FLAN-T5 / GPT                         |
| Backend             | Python                                        |
| Deployment          | Flask / FastAPI / Streamlit                   |

---

📁 **Project Structure**

multilingual-healthcare-chatbot
│
├── models
│   ├── symptom_dictionary.json
│   └── gpt_model
│
├── src
│   ├── language_detection.py
│   ├── translation.py
│   ├── symptom_extraction.py
│   ├── response_generator.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── app.py or notebook.ipynb

---

⚙️ **Installation & Setup**

1. Clone the repository
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name

2. Install dependencies
   pip install -r requirements.txt

3. Run the chatbot
   python main.py

For the web/app version:
python app.py

---

💡 **How It Works**

1. Language Detection
   lang = detect(user_input)

2. Translate to English
   english_text = translator.translate(user_input, dest="en")

3. Extract Symptoms
   extracted = extract_symptoms(english_text)

4. Generate Response Using GPT
   response = gpt_model.generate(english_text)

5. Translate Back to User Language
   final_output = translator.translate(response, dest=lang)

---

🧪 **Example Conversation**

User (Hindi):
"मुझे सिर दर्द और चक्कर आ रहे हैं, क्या करना चाहिए?"

Bot:
"आप आराम करें, पानी पिएं, और यदि दर्द बना रहे तो डॉक्टर से संपर्क करें। यह डिहाइड्रेशन या माइग्रेन का संकेत हो सकता है."

---

📌 **Future Enhancements**

* Add more Indian languages
* Integrate a medical diagnosis model
* Add voice input/output
* Create Streamlit UI
* Connect patient history for contextual answers

---

🤝 **Contributing**

Pull requests are welcome.
For major changes, please open an issue first to discuss what you want to update.

---

📄 **License**

MIT License

---

🔗 **GitHub Link**

[[https://github.com/yourusername/your-repo-name](https://github.com/yourusername/your-repo-name)](https://github.com/pritam-09/Multilingual_Healthcare_Chatbot.git)

