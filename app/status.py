from app import app
from flask import render_template
from app import values

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", server = 'rio', uptime = values.uptime(), user = 'skasturi', load = values.loadaverage(), memory = '1 GB')

