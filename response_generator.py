# from transformers import GPT2Tokenizer, GPT2LMHeadModel

# def generate_response(input_text):
#     # Adding a prompt to specify that the model should respond with healthcare advice
#     prompt = f"Provide healthcare advice for the following symptoms: {input_text}. Please suggest medical advice that is relevant."

#     model_name = 'gpt2'  # Using a smaller model like 'gpt2' for performance
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPT2LMHeadModel.from_pretrained(model_name)

#     # Set the pad_token to eos_token (end-of-sequence token) if not already set
#     tokenizer.pad_token = tokenizer.eos_token

#     # Tokenize input text with truncation
#     inputs = tokenizer.encode(prompt, return_tensors='pt', max_length=512, truncation=True, padding=True)

#     # Generate response with temperature and top_p for better diversity
#     outputs = model.generate(inputs, max_length=100, num_return_sequences=1, pad_token_id=50256,
#                              temperature=0.7, top_p=0.9, do_sample=True)

#     # Decode and return the response
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return response.strip()
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Initialize tokenizer and model
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the pad_token to be the eos_token
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_response(input_text):
    # Encode the input text
    inputs = tokenizer.encode(input_text, return_tensors='pt', max_length=512, padding=True, truncation=True)
    
    # Generate the response
    outputs = model.generate(
        inputs, 
        max_length=100, 
        num_return_sequences=1, 
        pad_token_id=tokenizer.pad_token_id,  # Use the pad_token_id
        temperature=0.7,  # Adjust temperature for controlled randomness
        no_repeat_ngram_size=2,  # Avoid repetition
        top_k=50,  # Use top-k sampling for more diverse results
        top_p=0.95,  # Use nucleus sampling for more diverse results
        do_sample=True  # Allow sampling for more varied responses
    )

    # Decode and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
