# 🤖 Chatbot with Memory – Python & Hugging Face Transformers

A beginner-friendly chatbot built with Python using the Hugging Face `transformers` library. This chatbot can hold simple memory of past conversation turns and responds using a pre-trained model (`facebook/blenderbot_small-90M`). Perfect as a hands-on intro project into LLMs and conversational AI.


## 📂 Project Structure

```

chatbot/
├── chatbot\_with\_memory.py       # Main chatbot script using BlenderBot
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── venv/                        # Virtual environment (excluded from version control)

````

---

## 🚀 Features

- Uses a **pre-trained conversational model** from Hugging Face (`Blenderbot Small`).
- Maintains **simple conversational history** to provide slightly context-aware responses.
- Easy to extend or swap with other Hugging Face models.
- Clean CLI-based interface.

---

## 🧠 Model Info

- **Model Used**: [`facebook/blenderbot_small-90M`](https://huggingface.co/facebook/blenderbot_small-90M)
- **Library**: `transformers` by Hugging Face
- This model is small (~90MB), making it lightweight enough for experimentation on personal machines.

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

### 4. Run the chatbot

```bash
python chatbot_with_memory.py
```

---

## 💬 Example Conversation

```
You can start chatting with the bot (type 'exit' to quit)

You: hi, who are you?
Bot: I am a helpful assistant.

You: what's your name?
Bot: I'm called Bot.

You: what is 2 + 2?
Bot: 2 + 2 is 4.

You: bye
Bot: Goodbye! Talk to you later.
```

---

## 🛠️ Requirements

Make sure your internet is working (for model download), or pre-download the model if needed.

```
transformers>=4.40.0
torch>=2.1.0
```

If needed, generate a fresh `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 🧪 Future Improvements

* Add **local fallback model** when internet is unavailable.
* Implement **GUI** (Tkinter or web-based like Streamlit).
* Add support for **web search**, **retrieval-augmented generation**, or **voice input/output**.
* Integrate with **LangChain** or **LLM APIs** for more power.

---

## 🧠 Learning Goals

This repo is ideal for:

* Beginners learning about **LLMs**
* Experimenting with **Hugging Face Transformers**
* Building your first **memory-aware chatbot**

---

## 📄 License

MIT License. Feel free to fork, reuse, and build on it!

---

## 🙌 Acknowledgments

* [Hugging Face Transformers](https://github.com/huggingface/transformers)
* [Facebook AI – BlenderBot](https://ai.facebook.com/blog/blender-a-chatbot-that-can-chat-about-nearly-anything/)

