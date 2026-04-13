# Aura AI ✨
#### Video Demo: <URL HERE>
## 🌐 Live Demo
https://aura-ai-swk7.onrender.com/

#### Description:

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-purple)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-red)

## Screenshots

### 💬 Chat Interface
![Chat UI](screenshots/chat.png)

### 🧠 Conversation Example
![Conversation](screenshots/conversation.png)

## What is Aura AI?

Aura AI is an AI-powered chatbot web application I built as my final project for CS50P — Harvard University's Introduction to Programming with Python. It runs in the browser, looks clean and modern, and lets you have real conversations with an AI assistant powered by Groq's LLaMA 3 model.
The application provides a modern browser-based chat interface and integrates with Groq’s LLaMA 3 model to deliver fast, real-time AI responses.

## Features

- 💬 Real-time AI conversations
- 🧠 Remembers full conversation history
- 🌙 Sleek dark mode UI inspired by ChatGPT
- ⚡ Super fast responses powered by Groq
- 🎨 Clean chat bubbles with avatars
- ✨ Personalised AI personality as Aura AI

## How It Works

You open the app in your browser, type a message, and Aura AI replies almost instantly. Your message gets sent to a Flask backend, added to the conversation history, and forwarded to the Groq API. The response comes back and appears as a chat bubble on the screen. Aura AI remembers the full conversation throughout your session so it always has context of what you said earlier.

## Project Files

**project.py** — The heart of the project. Contains the Flask server, Groq API connection, and four main functions:
- `get_response()` — calls the Groq AI API and returns the reply
- `format_message()` — structures each message correctly for the API
- `get_system_prompt()` — defines Aura AI's personality and identity
- `main()` — starts the Flask development server

**templates/index.html** — The entire frontend of the application. Dark ChatGPT-style interface with chat bubbles, avatars, and a fixed input bar at the bottom. All HTML, CSS and JavaScript written by me from scratch.

**test_project.py** — Contains all pytest tests for the project. Tests `format_message()`, `get_system_prompt()` and `get_response()` to make sure everything works correctly.

**requirements.txt** — Lists all dependencies needed to run the project.

**.env** — Stores the Groq API key securely. Never pushed to GitHub.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| Flask | Web framework |
| Groq API | AI model (LLaMA 3) |
| python-dotenv | Environment variable management |
| HTML/CSS/JS | Frontend interface |

## Design Decisions

I originally planned to use OpenAI's API but switched to Groq because it is completely free and has very fast response times. I also chose to build a web interface with Flask instead of keeping it as a CLI app because a browser app is much more impressive to demo and feels like a real product.

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/xaviercop/Aura-ai.git
cd aura-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Groq API key:

GROQ_API_KEY=your-key-here


4. Run the app:
```bash
python3 project.py
```

5. Open your browser and go to:
http://127.0.0.1:5000


## Running Tests

```bash
pytest test_project.py
```

## About

Made by **Afnan Adnan** from Pakistan 🇵🇰 as a final project for CS50P — Harvard University's Introduction to Programming with Python.

This was CS50P! ✨🎉
