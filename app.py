import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

class ChatbotWithMemory:
    def __init__(self, max_history=5, max_tokens=512):
        self.max_history = max_history
        self.max_tokens = max_tokens
        self.system_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."

    def generate_response(self, user_input, history):
        if history is None:
            history = []

        prompt = self._build_prompt(user_input, history)

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
        history.append((user_input, response))

        # Truncate if needed
        if len(history) > self.max_history:
            history = history[-self.max_history:]

        return response, history

    def _build_prompt(self, user_input, history):
        prompt_parts = [self.system_prompt]
        for exchange in history:
            prompt_parts.append(f"User: {exchange[0]}")
            prompt_parts.append(f"Assistant: {exchange[1]}")
        prompt_parts.append(f"User: {user_input}")
        prompt_parts.append("Assistant:")

        full_prompt = "\n".join(prompt_parts)
        tokens = tokenizer.encode(full_prompt)

        if len(tokens) > self.max_tokens:
            excess = len(tokens) - self.max_tokens
            truncated_tokens = tokens[excess:]
            full_prompt = tokenizer.decode(truncated_tokens, skip_special_tokens=True)

        return full_prompt

chatbot = ChatbotWithMemory()

def chat_fn(user_input, history):
    response, updated_history = chatbot.generate_response(user_input, history)
    return response, updated_history

iface = gr.Interface(
    fn=chat_fn,
    inputs=["text", "state"],
    outputs=["text", "state"],
    title="Flan-T5 Chatbot with Contextual Memory",
    description="A chatbot using FLAN-T5 that remembers the last few exchanges."
)

if __name__ == "__main__":
    iface.launch(share=True)
