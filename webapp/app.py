import os
from flask import Flask, render_template, jsonify
from horoscope import horoscope

app = Flask(__name__)

# configuration
DEBUG = True
app.config.from_object(__name__)


@app.route('/')
def index():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/gen', methods=['GET', 'POST'])
def gen():
    return horoscope.generate()


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return jsonify({'fortune': horoscope.generate()})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)