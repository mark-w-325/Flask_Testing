from flask import render_template
from test_app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/header')
def header():
    return render_template('header.html')


@app.route('/test')
def test():
    return render_template('test.html')
