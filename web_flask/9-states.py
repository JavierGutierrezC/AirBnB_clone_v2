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


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:iden>', strict_slashes=False)
def states_id(iden=None):
    """print cities ans State"""
    objetos = storage.all("State")
    c_dit = {}
    s_dit = {}
    if iden is None:
        for key, values in objetos.items():
            if "State" in key:
                s_dit[key] = values
        return render_template("7-states_list.html", new_dict2=s_dit)
    else:
        for key, values in objetos.items():
            if "State" in key:
                if values.id == iden:
                    s_dit[key] = values
            if "City" in key:
                if values.state_id == iden:
                    c_dit[key] = values
        return render_template("9-states.html", city=c_dit, state=s_dit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
