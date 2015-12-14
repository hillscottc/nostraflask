

A Flask interface for Nostradamuss, hosted on [heroku](https://nostraflask.herokuapp.com/).

# Build
Clone this repo. Then, the app can be installed/run locally with pip, or as a [Docker](https://www.docker.com/) image.

## pip local
Create a python virtual environment with [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).
Then install and run with:

    pip install -r webapp/requirements.txt
    python webapp/app.py

## Docker

    docker build -t your_name/nostraflask .
    docker run -d -P your_name/nostraflask python app.py

# Test
I'm using [Nose](http://nose.readthedocs.org/en/latest/). 

    nosetests
    

    


