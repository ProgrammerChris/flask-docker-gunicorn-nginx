from flask import render_template
import os
from app import app


@app.route("/")
def index():
    return render_template('index.html')
