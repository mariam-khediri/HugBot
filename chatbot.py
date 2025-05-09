from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Step 1: Choose a model
MODEL_NAME = "google/flan-t5-base"

# Step 2: Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Step 3: Define response generation function
def generate_response(user_input):
    """
    Generates a response from the model based on user input.
    """

    # Step 4: Tokenize the input prompt
    inputs = tokenizer(user_input, return_tensors="pt")  # pt = PyTorch tensors

    # Step 5: Model inference (generate output tokens)
    outputs = model.generate(
        **inputs,
        max_length=200,         # Limit output size
        num_return_sequences=1, # One answer
        do_sample=True,         # Add randomness (more human-like)
        temperature=0.7         # Controls randomness (0 = deterministic, 1 = very random)
    )

    # Step 6: Decode tokens to human-readable string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot:", generate_response(user_input))
