from flask import Flask, render_template, request
from datetime import date
import time
from DAL import *


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my Inventory!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/inventory/')
def inventory():
    return F'<html><body><h1> { get_items()}<h1><body><html>'

@app.route('/insertitem', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['category']
        data3 = request.form['quantity']
        data4 = request.form['price']
        insert_item(data, data2, data3, data4,date.today())      
        return render_template('insertitem.html', data=data)
    
    return render_template('insertitem.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


