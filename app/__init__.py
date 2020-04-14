from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "r@ndomkey123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://psoqugvkylzpkb:8a40e259c96cff288e8faae8c52dccf7086248046549a6ac2e7d7db9c50f96a7@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d4bn6pp7fai1k5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
