from flask import Flask, render_template

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
    app.run(debug=True)
