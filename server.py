from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "98fc348fdd1d8714135faf775517a0b0382ff6b2e164d0ff28b1b81855f5109d"


@app.route("/")
def index():
    """Route displays form"""
    return render_template("index.html")


@app.post("/process")
def process():
    """This route processes the form"""
    print("Name:", request.form["name"])
    print("Location:", request.form["location"])
    print("Favorite Langauge:", request.form["language"])
    print("Comments:", request.form["comments"])

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")


@app.get("/results")
def results():
    """Route displays results"""
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
