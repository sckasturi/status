from app import app
from flask import render_template
from app import values

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", server = values.hostname(), uptime = values.uptime(), user = values.users(), load = values.loadaverage(), memory = values.memory())

