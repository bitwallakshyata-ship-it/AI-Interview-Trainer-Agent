from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    questions = []
    feedback = ""
    report = ""

    if request.method == "POST":

        role = request.form.get("role", "")
        skills = request.form.get("skills", "")
        interview_type = request.form.get("interview_type", "")
        answer = request.form.get("answer", "")

        if interview_type == "HR":
            questions = [
                "Tell me about yourself.",
                "Why should we hire you?",
                "What are your strengths?",
                "What are your weaknesses?",
                "Where do you see yourself in 5 years?"
            ]

        elif interview_type == "Technical":
            questions = [
                f"What are the key concepts of {skills}?",
                f"Explain a project where you used {skills}.",
                f"What challenges did you face while using {skills}?",
                "What is Object Oriented Programming?",
                "How do you debug code?"
            ]

        elif interview_type == "Behavioral":
            questions = [
                "Describe a difficult situation you handled.",
                "Tell me about a time you worked in a team.",
                "How do you manage deadlines?",
                "Describe a conflict and how you resolved it.",
                "Tell me about a leadership experience."
            ]

        if answer:

            words = len(answer.split())

            if words < 20:
                score = 4
            elif words < 40:
                score = 6
            elif words < 60:
                score = 8
            else:
                score = 10

            feedback = f"""
Score: {score}/10

Strengths:
✔ Good effort
✔ Relevant response

Areas for Improvement:
✔ Add specific examples
✔ Mention achievements
✔ Improve structure
"""

            report = f"""
Overall Performance Report

Final Score: {score}/10

Strong Areas:
✔ Communication
✔ Confidence

Needs Improvement:
✔ More detailed answers
✔ Technical depth
"""

    return render_template(
        "index.html",
        questions=questions,
        feedback=feedback,
        report=report
    )

if __name__ == "__main__":
    app.run(debug=True)
