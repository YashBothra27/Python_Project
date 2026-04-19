from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")

        if expression.strip():
            result = calc.evaluate(expression)

    history = calc.get_history()

    return render_template(
        "index.html",
        result=result,
        history=history,
        expression=expression
    )

if __name__ == "__main__":
    app.run()