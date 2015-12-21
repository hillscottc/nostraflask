import os
from flask import Flask, render_template, jsonify
from webapp.horoscope import horoscope

application = Flask(__name__)

# configuration
DEBUG = True
application.config.from_object(__name__)


@application.route('/')
def index():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@application.route('/home')
def home():
    return render_template('home.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/hello/')
@application.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@application.route('/gen', methods=['GET', 'POST'])
def gen():
    return horoscope.generate()


@application.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return jsonify({'fortune': horoscope.generate()})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)