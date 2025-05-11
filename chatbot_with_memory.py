from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

class ChatbotWithMemory:
    def __init__(self, max_history=3):
        self.conversation_history = []
        self.max_history = max_history
        self.system_prompt = "You are a helpful AI assistant. Answer the user's questions clearly and politely."
    
    def generate_response(self, user_input):
        # Build the prompt with context
        prompt = self._build_prompt(user_input)
        
        inputs = tokenizer(prompt, return_tensors="pt")
        
        outputs = model.generate(
            **inputs,
            max_length=100,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Update history (avoid adding empty responses)
        if response.strip():
            self._update_history(user_input, response)
        
        return response
    
    def _build_prompt(self, user_input):
        # Start with system instruction
        prompt_parts = [self.system_prompt]
        
        # Add conversation history (without labels)
        for user_msg, bot_msg in self.conversation_history[-self.max_history:]:
            prompt_parts.append(f"User: {user_msg}")
            prompt_parts.append(f"Assistant: {bot_msg}")
        
        # Add current input
        prompt_parts.append(f"User: {user_input}")
        prompt_parts.append("Assistant:")
        
        return "\n".join(prompt_parts)
    
    def _update_history(self, user_input, response):
        self.conversation_history.append((user_input, response))
        # Keep history within bounds
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]

if __name__ == "__main__":
    chatbot = ChatbotWithMemory()
    print("Chatbot with memory started. Type 'exit' or 'quit' to end.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        response = chatbot.generate_response(user_input)
        print("Bot:", response)