import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    