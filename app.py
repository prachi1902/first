import os
# Import Flask for creating API
from flask import Flask, request
port = int(os.environ.get('PORT', 5000))


# Initialise a Flask app
app = Flask(__name__)
# Create an API endpoint
    
@app.route('/echo')

def run():
    data=request.args.get('test')
    return data

@app.route('/name')

def run1():
    name1=request.args.get('fname')
    name2=request.args.get('sname')
    name="Your name is " + str(name1) + " " +str(name2)
    return name


if __name__ == '__main__':
	app.run() 