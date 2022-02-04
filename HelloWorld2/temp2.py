from flask import Flask, redirect, url_for, request, render_template, make_response
app = Flask(__name__)

@app.route('/')

def index():
   return redirect('http://www.example.com')
   #response = make_response('<h1>This document carries a cookie!</h1>')
   #response.set_cookie('answer', '42')
   #return response

#def index():
#    #return '<h1>Hello World!</h1>'
#    return render_template('html10.html')

def index1():
   return '<h1>Hello World!</h1>'

def index2():
   return '<h1>Hello World New!</h1>'

def index4():
   return '<h1>Hello World New vccbvnfj!</h1>'


app.add_url_rule('/test', 'index4', index4)


@app.route('/qwert')

def index3():
   return '<h1>Hello World BCD!</h1>'

@app.route('/user/<name>')
def user(name):
   return render_template('html10.html', name='')
   #return '<h1>Hello, {}!</h1>'.format(name)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082)