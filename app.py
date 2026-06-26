from flask import Flask, render_template, request

from document_loader import load_numbered_chunks
from retriever import retrieve_chunk
from prompts import build_prompt
from gemini_client import ask_gemini
from validator import validate_answer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    source = ""
    question = ""

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if question:

            chunks = load_numbered_chunks()

            best_chunk = retrieve_chunk(question, chunks)

            if best_chunk:

                prompt = build_prompt(
                    best_chunk["text"],
                    question
                )

                answer = ask_gemini(prompt)

                answer = validate_answer(answer)

                if answer != "Information Not Found":
                    source = f"Paragraph {best_chunk['id']}"

    return render_template(
        "index.html",
        answer=answer,
        source=source,
        question=question
    )


if __name__ == "__main__":
    app.run(debug=True)