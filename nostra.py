import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from horoscope import horoscope

SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    

@app.route('/gen')
def gen():
    return horoscope.generate()   

if __name__ == '__main__':
    app.run(debug=True)


    