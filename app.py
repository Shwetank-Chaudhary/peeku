from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/memories")
def memories():
    return render_template("memories.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/valentine")
def valentine():
    return render_template("valentine.html")

@app.route("/finally")
def final():
    return render_template("finally.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's assigned port, fallback to 5000 for local testing
    app.run(host="0.0.0.0", port=port)
