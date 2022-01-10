# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


#@app.route('/')
#def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
#    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
#                   datetime.datetime(2018, 1, 2, 10, 30, 0),
#                   datetime.datetime(2018, 1, 3, 11, 0, 0),
#                   ]

#    return render_template('html3.html', times=dummy_times)

@app.route('/')
def Hello():
    """Return a friendly HTTP greeting."""

    return '''
        Enter your name
        <form method="get" action="reverse_string">
            <p><input type=text name=string value="">
            <p><input type=submit>
        </form>
        
    '''

@app.route('/reverse_string', methods=['GET'])
def ReverseString():
    try:
        s = str(request.args.get('string'))
    except Exception as e:
        print(e)
        return 'Not a valid string!'

    current = StringProcessor(s).Reverse()
    expected = s[::-1]
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    text1 = "Hello";
    text2 = 'string';
    text3 = "How are you today!";
    #names = text1.concat(text3);
    names = "Hello everyone";

    #return s
    return render_template('html5.html', times=names)
# There is a bug in the code.
class StringProcessor():
    def __init__(self, string):
        self._string = string

    def Reverse(self):
        if self._string == '':
            return ''

        chars = [c for c in self._string]
        left = 0
        right = len(chars) - 1
        while True:
            tmp = chars[left]
            chars[left] = chars[right]
            chars[right] = tmp
            if left >= right:
                break
            left += 1
            right -= 1

        return ''.join(chars)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
