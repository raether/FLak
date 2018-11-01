#!/usr/local/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/cakes')
def cakes():
    return 'Yummy Cakes'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
