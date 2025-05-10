from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load tokenizer and model
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Store conversation history
conversation_history = []

print("You can start chatting with the bot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add user input to history
    conversation_history.append(f"User: {user_input}")

    # Combine last few messages for context (e.g., last 5 turns)
    prompt = "\n".join(conversation_history[-5:]) + "\nBot:"

    # Tokenize and generate response
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Show and store bot response
    print(f"Bot: {response}")
    conversation_history.append(f"Bot: {response}")
