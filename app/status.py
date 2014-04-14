from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", server = 'rio', uptime = '42 days', user = 'skasturi', load = '0.12, 0.10, 0.14', memory = '1 GB')

