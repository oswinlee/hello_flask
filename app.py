from flask import Flask, render_template
from datetime import datetime
import re
#hello for tesing github

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

#@app.route("/hello", defaults={'name':'Oswinlee'})
@app.route("/hello/")
@app.route("/hello/<name>")
#default value is oswinlee for name variable
def hello_there(name='oswinlee'):
    return render_template(
        "hello_there.html",
        name = name,
        date = datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")