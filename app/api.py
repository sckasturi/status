from app import values, app
from flask import jsonify, abort

val_dict = { 
    'hostname': values.hostname(), 
    'uptime': values.uptime(),
    'users': values.users(),
    'loadaverage': values.loadaverage(),
    'memory': values.memory()
}

@app.route('/api/<value>', methods = ['GET'])
def api(value):
    if not value in val_dict.keys():
        abort(404)
    return jsonify({ value: val_dict[value] })

@app.route('/api', methods = ['GET'])
def list():
    return jsonify(val_dict)
