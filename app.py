from flask import Flask
from DAL import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello DevOps Class</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/inventory/')
def inventory():
    return f'<h1> {get_items()} </h1>'
    
if __name__ == '__main__':
    app.run(debug=True)


