from flask import Flask, render_template, session, request
from flask_debugtoolbar import DebugToolbarExtension
import jinja2



app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""
  

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show application form page"""
    
    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_response():
    """Show application response"""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")

    return render_template("application-response.html", 
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            position=position )



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

