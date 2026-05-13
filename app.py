from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import openai
import os

app = Flask(__name__)

# If you are using OpenAI / Azure, put your key in .env
# Example:
# OPENAI_API_KEY=your_key_here
openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(text):
    """
    Summarizes the given news text using OpenAI.
    Falls back to simple summary if API fails.
    """
    try:
        if not text.strip():
            return "Please enter some news text to summarize."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes news articles in a clear and concise way."
                },
                {
                    "role": "user",
                    "content": f"Summarize this news article in 5-6 lines:\n\n{text}"
                }
            ],
            max_tokens=200,
            temperature=0.5
        )

        summary = response["choices"][0]["message"]["content"]
        return summary.strip()

    except Exception as e:
        # Fallback summary (important for viva/demo)
        sentences = text.split(".")
        simple_summary = ". ".join(sentences[:3])
        return simple_summary if simple_summary else f"Summarization Error: {str(e)}"


def translate_text(text, target_language):
    """
    Translates the summary into selected language.
    """
    try:
        if target_language == "en":
            return text  # No translation needed

        translated = GoogleTranslator(
            source="auto",
            target=target_language
        ).translate(text)

        return translated

    except Exception as e:
        return f"Translation Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    original_text = ""
    selected_language = "en"

    if request.method == "POST":
        # Get form data
        original_text = request.form.get("news_text", "")
        selected_language = request.form.get("language", "en")

        if original_text.strip():
            # Step 1: Summarize
            summary = summarize_text(original_text)

            # Step 2: Translate (if not English)
            summary = translate_text(summary, selected_language)
        else:
            summary = "⚠️ Please paste a news article to summarize."

    return render_template(
        "index.html",
        summary=summary,
        original_text=original_text,  # IMPORTANT: keeps text in textarea
        selected_language=selected_language
    )


if __name__ == "__main__":
    app.run(debug=True)