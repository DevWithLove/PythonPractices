from flask import Flask
from decorator_ex import *

"""
if run in ternmial 
export FLASK_APP=hello.py
flask run
https://flask.palletsprojects.com/en/2.3.x/quickstart/
"""
app = Flask(__name__)


@app.route("/") #Python decorators
@make_bold
@make_emphasis
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! you are {number}"

# if we are running the code in the current file
if __name__ == "__main__":
     app.run(debug=True,host='0.0.0.0', port=5001) # same as in Terminal 'flask run'

