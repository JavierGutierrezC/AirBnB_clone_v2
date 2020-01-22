#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from  models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_airbnb():
    objects = storage.all(State)
    print(objects)
    # new_list
    return render_template('7-states_list.html', new_list=new_list)

@app.teardown_appcontext
def SQL_close(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()
