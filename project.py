import os
from dotenv import load_dotenv
from groq import Groq
from flask import Flask, render_template, request, jsonify

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = Flask(__name__)

def format_message(role, content):
    return {"role": role, "content": content}

def get_system_prompt():
    return """You are a helpful and friendly AI assistant called "Aura AI", created by Afnan Adnan as a CS50P final project.

    If anyone asks who created you, say "Afnan Adnan created me as part of their CS50P final project at Harvard."
    If anyone asks what your name is, say "My name is Aura AI! ✨"
    If anyone asks what you are, say "I am Aura AI, an intelligent chatbot built with Python, Flask and Groq AI. ✨"
    If anyone asks what CS50P is, say "CS50P is Harvard University's Introduction to Programming with Python course."

    Always be helpful, friendly and concise in your responses."""

def get_response(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

messages = [format_message("system", get_system_prompt())]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    messages.append(format_message("user", user_input))
    response = get_response(messages)
    messages.append(format_message("assistant", response))
    return jsonify({"response": response})

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
