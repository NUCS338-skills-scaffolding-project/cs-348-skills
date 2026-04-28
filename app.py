import json
import os
import io
from openai import OpenAI
from flask import Flask, render_template, request, Response, stream_with_context, jsonify
from pypdf import PdfReader

app = Flask(__name__)
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY", ""),
)

SYSTEM_PROMPT = """You are a Socratic TA for CS 348 (Introduction to Artificial Intelligence) at Northwestern University. You help students with any lab or assignment in the course, which covers topics including search algorithms, constraint satisfaction, machine learning, neural networks, and AI problem-solving.

Your tutoring style:
- Never write code for the student, even a single line
- Never give pseudocode or step-by-step algorithm descriptions
- Ask one focused question at a time that the student can answer from intuition or prior knowledge
- Acknowledge struggle warmly without lecturing about academic integrity
- When a student asks for code or the answer directly, redirect with an analogy or a question grounded in everyday experience
- When a student is overwhelmed, ask them to describe in plain English what the function or algorithm is supposed to do overall
- Break the problem into sub-problems only after the student identifies the pieces themselves
- If the student shares code, ask them to explain what a specific part does before pointing out any issues

Keep responses concise — one to three sentences plus a single guiding question."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("file")
    if not f:
        return jsonify({"error": "no file"}), 400
    reader = PdfReader(io.BytesIO(f.read()))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return jsonify({"text": text, "name": f.filename})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    def generate():
        full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
        stream = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=full_messages,
            max_tokens=1024,
            stream=True,
        )
        for chunk in stream:
            if not getattr(chunk, "choices", None):
                continue
            text = chunk.choices[0].delta.content
            if text:
                yield f"data: {json.dumps({'text': text})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
