from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset once
data = pd.read_csv("clean_student.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    person = None
    error = None

    if request.method == "POST":
        try:
            order_id = int(request.form["order_id"])

            person = data[data["order_id"] == order_id]

            if person.empty:
                error = "No person found with that Order ID"

        except:
            error = "Invalid input. Please enter a number."

    return render_template("index.html", person=person, error=error)

if __name__ == "__main__":
    app.run(debug=True)