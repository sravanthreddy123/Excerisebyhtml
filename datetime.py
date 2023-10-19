from flask import Flask
from flask import render_template
from datetime import datetime

@app.route('/example')
def example():
    return render_template('template.html', datetime = str(datetime.now()))

app = Flask(__name__)

@app.route('/')
def index():
    return show_home()


def show_home():
    return render_template('index.html')

@app.route('/ingredients/')
def ingredients():
    return show_ingredients()

def show_ingredients():
    return render_template('ingredients.html')

@app.route('/cooking_instructions/')
def cook_it():
    return show_cook_it()

def show_cook_it():
    return render_template('cooking_instructions.html')
