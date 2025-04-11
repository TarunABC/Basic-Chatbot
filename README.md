# Basic-Chatbot
# JSON-Based Learnable Chatbot 🤖

This is a simple, command-line chatbot built using Python. It uses a JSON file as a knowledge base and learns new responses when it encounters unknown questions.

---

## 🚀 Features

- Uses a JSON file to store Q&A pairs
- Matches user questions using fuzzy logic (close match detection)
- Learns new answers interactively from the user
- Saves learned knowledge for future sessions
- Lightweight and beginner-friendly

---

## 🧠 How It Works

1. The bot loads a list of question-answer pairs from `knowledge_base.json`.
2. It uses `difflib.get_close_matches()` to find the closest known question.
3. If it finds a match, it returns the stored answer.
4. If not, it asks the user to teach it, and then stores the new answer.
5. You can exit the chatbot
