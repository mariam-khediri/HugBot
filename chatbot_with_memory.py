from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

class ChatbotWithMemory:
    def __init__(self, max_history=5, max_tokens=512):
        self.conversation_history = []
        self.max_history = max_history
        self.max_tokens = max_tokens
        self.system_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    
    def generate_response(self, user_input):
        # Prepare the prompt with history
        prompt = self._build_prompt(user_input)
        
        inputs = tokenizer(prompt, return_tensors="pt")
        
        outputs = model.generate(
            **inputs,
            max_length=200,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Update history
        self._update_history(user_input, response)
        
        return response
    
    def _build_prompt(self, user_input):
        # Start with system prompt
        prompt_parts = [self.system_prompt]
        
        # Add conversation history
        for exchange in self.conversation_history[-self.max_history:]:
            prompt_parts.append(f"User: {exchange[0]}")
            prompt_parts.append(f"Assistant: {exchange[1]}")
        
        # Add current input
        prompt_parts.append(f"User: {user_input}")
        prompt_parts.append("Assistant:")
        
        # Join and truncate if needed
        full_prompt = "\n".join(prompt_parts)
        tokens = tokenizer.encode(full_prompt)
        
        if len(tokens) > self.max_tokens:
            # Truncate from the beginning (oldest messages)
            excess = len(tokens) - self.max_tokens
            truncated_tokens = tokens[excess:]
            full_prompt = tokenizer.decode(truncated_tokens, skip_special_tokens=True)
        
        return full_prompt
    
    def _update_history(self, user_input, response):
        self.conversation_history.append((user_input, response))
        # Keep history within bounds
        if len(self.conversation_history) > self.max_history * 2:  # *2 for user+bot pairs
            self.conversation_history = self.conversation_history[-self.max_history * 2:]

if __name__ == "__main__":
    chatbot = ChatbotWithMemory()
    print("Chatbot with memory started. Type 'exit' or 'quit' to end.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        response = chatbot.generate_response(user_input)
        print("Bot:", response)