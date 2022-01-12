import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Hello():
    """Entering name."""

    return '''
        Enter your name
        <form method="get" action="welcome">
            <p><input type=text name=string value="">
            <p><input type=submit>
        </form>
        
    '''

@app.route('/welcome', methods=['GET'])
def Welcome():
    try:
        s = str(request.args.get('string'))
    except Exception as e:
        print(e)
        return 'Not a valid string!'


    if s == "Jaideep":
        usertemp = "Jaideep Banerjee"
    elif s == "Gabriele":
        usertemp = "Gabriele M"
    else:
        usertemp = s


    return render_template('html5.html', user=usertemp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
