#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_airbnb():
    objects = storage.all("State")
    # print(objects)
    new_dict = {}
    for x in objects.keys():
        if "State" in x:
            # print(x)
            new_dict[x] = objects[x]
    # print(new_dict)
    return render_template('7-states_list.html', new_dict2=new_dict)


@app.teardown_appcontext
def SQL_close(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
