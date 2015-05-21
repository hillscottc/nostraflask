from flask import Flask, jsonify, render_template
from horoscope import horoscope

SECRET_KEY = 'development key'

NOSE_ARGS = [
    '--detailed-errors', '--verbosity=2',
    '--nocapture', '--nologcapture',
    #'--failed',  # Run tests that failed in the last run.
    #'--stop',    # Stop at first failure.
    # '--pdb',
]

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
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
    app.run(debug=True)

