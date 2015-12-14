from flask import Flask, jsonify, render_template
from horoscope import horoscope

SECRET_KEY = 'development key'

#  nostra
# Access Key ID: AKIAJS5ACOYR74MHBZVQ
# Secret Access Key:  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

application = Flask(__name__)
application.config.from_object(__name__)


@application.route('/')
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
    application.debug = True
    application.run(debug=True)

