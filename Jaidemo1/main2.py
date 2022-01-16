import datetime
import Users

from flask import Flask, render_template, request
from subprocess import call

app = Flask(__name__)

'''
class CallPy(object):
    def __init__(self,path="/Users/jbanerjee/PycharmProjects/pythonProject/Jaidemo1/Users.py"):
        self.path = path

    def call_users(self):
        call(["Python3", "{}".format(self.path)])
'''


if __name__ == '__main__':
    print(Users.x)
    #app.run(host='127.0.0.1', port=8081, debug=True)
    #c = CallPy()
    #c.call_users()
