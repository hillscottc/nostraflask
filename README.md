

A Flask interface for Nostradamuss, hosted on [heroku](https://nostraflask.herokuapp.com/).

# Build
- Clone this repo

# Run locally
Create a python virtual environment with [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).
Then install and run with:

    pip install -r webapp/requirements.txt
    python webapp/app.py

# Run Docker image

    docker run -d -P hillscottc/nostraflask:v4 python app.py

# Test
I'm using [Nose](http://nose.readthedocs.org/en/latest/). 

    nosetests
    

    


