from flask import Flask, render_template, request
from translator import translate_speech

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    original = ""
    translated = ""

    if request.method == "POST":
        original, translated = translate_speech()

    return render_template("index.html",
                           original=original,
                           translated=translated)

if __name__ == "__main__":
    app.run(debug=True)