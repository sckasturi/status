from app import app
from flask import render_template
from app import values

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", server = values.hostname(), uptime = values.uptime(), users = values.users(), load = values.loadaverage(), memory = values.memory())

@app.route('/robots.txt')
def robots():
    return 'user-agent: * Disallow: /'

