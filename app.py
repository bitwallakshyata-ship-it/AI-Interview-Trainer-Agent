from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    questions = []

    if request.method == "POST":

        role = request.form["role"]
        skills = request.form["skills"]

        questions = [
            f"Tell me about yourself as a {role}.",
            f"What are the important concepts of {skills}?",
            f"Describe a project where you used {skills}.",
            f"What challenges can arise in the role of {role}?",
            f"Why should we hire you for this position?"
        ]

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)