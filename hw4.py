import glob, random
from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, image_info

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

image_folder = "/Users/mackinziewoodward/cst205/Homework/homework4/static/images"
image_files = glob.glob(f'{image_folder}')

@app.route('/')
def home():
    random.shuffle(image_files)
    random_images = image_files[:3]
    return render_template('index.html', random_images=random_images, image_info=image_info)
