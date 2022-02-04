from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = 'poster'))
   else:
      return (render_template('reglogin.html'))
      #user = request.args.get('nm')
      #return redirect(url_for('success',name = 'getter'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082)
