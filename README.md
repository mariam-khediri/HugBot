Thanks! Here's your updated `README.md` with **only the necessary additions and modifications**, reflecting the changes you've made (switch to `google/flan-t5-base`, Gradio UI, and enhanced memory support), while preserving your original structure and tone:

---

```md
# 🤖 Chatbot with Memory – Python & Hugging Face Transformers

A beginner-friendly chatbot built with Python using the Hugging Face `transformers` library. This chatbot can hold simple memory of past conversation turns and responds using a pre-trained model. Perfect as a hands-on intro project into LLMs and conversational AI.

---

## 📂 Project Structure

```

chatbot/
├── chatbot\_with\_memory.py       # Main chatbot logic with contextual memory
├── app.py                       # Gradio-based web interface
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── venv/                        # Virtual environment (excluded from version control)

````

---

## 🚀 Features

- Uses a **pre-trained conversational model** from Hugging Face (`FLAN-T5 Base`).
- Maintains **simple conversational history** for context-aware responses.
- Clean CLI interface **and** modern **Gradio web UI**.
- Easy to swap out models and extend with more capabilities.

---

## 🧠 Model Info

- **Model Used**: [`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base)
- **Library**: `transformers` by Hugging Face
- This model balances performance and speed, making it suitable for educational projects and light experimentation.

> 💡 *Note: The previously used model (`facebook/blenderbot_small-90M`) has been replaced to improve response quality.*

---

## ⚙️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/mariam-khediri/HugBot.git
cd Hugbot
````

### 2. Set up a virtual environment

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the CLI chatbot

```bash
python chatbot_with_memory.py
```

### 5. Or run the Gradio web app

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:7860`

---

## 💬 Example Conversation

```
You: Hi, who are you?
Bot: I'm your friendly AI assistant. How can I help you today?

You: What's 2 + 2?
Bot: 2 + 2 is 4.

You: And the capital of France?
Bot: The capital of France is Paris.
```

---

## 🛠️ Requirements

Ensure you have Python 3.8+ and an internet connection (for initial model download).

```
transformers>=4.40.0
torch>=2.1.0
gradio>=4.0.0
```

To regenerate the `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 🧪 Future Improvements

* Add **persistent memory** (e.g., database or embeddings-based memory).
* Add **voice input/output** using `gradio`'s audio features.
* Support **model selection** from the UI.
* Integrate with **LangChain**, **OpenRouter**, or other LLM APIs.

---

## 🧠 Learning Goals

This repo is ideal for:

* Beginners learning about **LLMs**
* Experimenting with **Hugging Face Transformers**
* Building your first **memory-aware chatbot**
* Exploring **Gradio** for quick UI prototyping

---

## 🙌 Acknowledgments

* [Hugging Face Transformers](https://github.com/huggingface/transformers)
* [Gradio by Hugging Face](https://gradio.app/)
* [Google FLAN-T5](https://huggingface.co/google/flan-t5-base)


