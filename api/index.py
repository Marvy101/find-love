from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'find love'}

@app.route('/about')
def about():
    return 'About'
