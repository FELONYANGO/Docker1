"""
@FELONYANGO
Module-level docstring providing an overview of the module.

This module modules is the main file and hanldes the logic of the COLOR count
when the button is clicked it prints a random color


"""

import random
from flask import Flask,render_template,request
from redis import Redis


app = Flask(__name__)
redis = Redis(host="redis",port=6379)


@app.route("/",methods=['GET','POST'])
def home():
    """
    This  function below handles the logics of the count,when the 
    button is clicked
    """
    color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    if request.method == 'POST':
        redis.incr('clicks')
    clicks = redis.get('clicks')
    if clicks is None:
        clicks = 0
    else:
        clicks = clicks.decode()
    return render_template('index.html', color=color, clicks=clicks)

@app.route("/hello")
def hello_world():
    """
     pass
    """
    return "the future is bright"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 ,debug=True)

