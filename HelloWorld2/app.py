# main program

import datetime
import webbrowser

# Users is user defined py file
import Users

from flask import Flask, redirect, url_for, request, render_template
from subprocess import call

app = Flask(__name__)


s = 2
username = " "
fname = " "
mname = " "
lname = " "
userid = " "
password = " "

# takes input from user
@app.route('/')
def Hello():
    """Entering name."""

    return '''
        If you a member of NOC and SOC team ?
        Type Yes and Proceed for registration <br> 
        <br> You may not have access of you are not a member of NOC and SOC team </br>
         
        <form method="get" action="welcome">
            <p><input type=text name=string value="">
            <p><input type=submit>
        </form>

    '''

@app.route('/welcome', methods=['GET'])
def Welcome():

    try:
        global s
        s = str(request.args.get('string'))
    except Exception as e:
        print(e)
        return 'Not a valid string!'

    if s == 'Yes':
        return render_template('reglogin.html',resp1=" Welcome New User", resp2="NOC and SOC Tool Upcoming")
    if s != 'Yes':
        return 'Sorry you may not have access to NOC and SOC application'


@app.route('/register')
def Register():
    return render_template('register.html')


@app.route('/login')
def Runurl1():
    #return render_template('login.html')
    return render_template('login.html')

    #return render_template('html5.html')

@app.route('/get-text', methods=['GET', 'POST'])
def registerhtml():
    global username
    global fname
    global mname
    global lname
    username = request.form['fname'] + '&nbsp;' + request.form['mname'] + '&nbsp;' + request.form['lname']
    fname = request.form['fname']
    mname = request.form['mname']
    lname = request.form['lname']

    id1 = Users.temp1(fname,mname,lname)
    print("inside", id1)
    return ("<br>" + "<b>" + "<big><big>" + '&nbsp;' +
            "Congratulations !!!" + '&nbsp;' +
            "<span style='color: red;'>" + username + "</span>" + '&nbsp;' +
            "You are now registered" + "</b>" + "</big>" + "<br><br>"
            '&nbsp;' + "Your userid is " + str(id1)
            )

@app.route('/get-login', methods=['GET', 'POST'])
def loginhtml():
    global userid
    global password

    userid = request.form['userid']
    password = request.form['password']

    resp = Users.temp3(userid, password)
    print(resp[0])
    print(resp[1])
    print(resp[2])

    if resp[0] == "User id do not exist":
        return (render_template("reglogin.html",resp1 = resp[0], resp2="Contact your system administrator" ))
        #return (resp[0])
    elif resp[1] == "Password do not match":
        return (render_template("reglogin.html",resp1 = resp[1], resp2="Contact your system administrator"))
    else:
        return (render_template("html5.html", resp = resp[2]))


@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('dailytracker.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)