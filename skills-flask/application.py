from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Shows the application form for a job at BallooniCorp"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_submission():
    """Show the user the application information they submitted."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = float(request.form.get("salary"))
    role = request.form.get("job-type")

    return render_template("application-response.html", first_name=first_name,
                                                        last_name=last_name,
                                                        salary=salary,
                                                        role=role)


if __name__ == "__main__":
    app.run(debug=True)
