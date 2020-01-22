#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def SQL_close(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_aibnb():
    """print cities ans State"""
    objetos = storage.all("State")
    c_dit = {}
    s_dit = {}
    for key, values in objetos.items():
        if "State" in key:
            s_dit[key] = values
        if "City" in key:
            c_dit[key] = values
    return render_template("8-cities_by_states.html", city=c_dit, state=s_dit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
