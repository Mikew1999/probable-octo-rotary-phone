''' Main URL routing '''
import os

# Imports required modules from Flask
from flask import (
    Flask, url_for,
    request, flash,
    redirect, render_template)

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


# Home page
@app.route("/")
def index():
    ''' Returns the home page '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
