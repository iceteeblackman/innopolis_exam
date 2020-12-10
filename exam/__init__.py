import os.path

from flask import Flask
from flask_autoindex import AutoIndex
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = os.environ['FOLDER']
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = 'some secret salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://itbm:_1q2w3e4r@172.17.0.2/innopolisapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
manager = LoginManager(app)
files_index = AutoIndex(app, os.environ['FOLDER'], add_url_rules=False)

from exam import models, routes

db.create_all()
