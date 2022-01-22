# main program

import datetime

# Users is user defined py file
import Users

from flask import Flask, render_template, request
from subprocess import call

app = Flask(__name__)


s = 2

# takes input from user
@app.route('/')
def Hello():
    """Entering name."""

    return '''
        Enter your id
        <form method="get" action="welcome">
            <p><input type=text name=string value="">
            <p><input type=submit>
        </form>

    '''

# extracts the id and send it to Users.py to fetch the name and role
@app.route('/welcome', methods=['GET'])
def Welcome():

# s contains the userid and declared global to be used in other files.

    try:
        global s
        s = str(request.args.get('string'))
    except Exception as e:
        print(e)
        return 'Not a valid string!'

# s is passed as a parameter to Users file in temp2 function
#name and role are returned from Users.py
    name,role = Users.temp2(s)
#name and role are passed to html5 to be displayed on the page
    return render_template('html5.html', user=name, role=role)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)



