from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#secret key for protection againt cookies
app.config['SECRET_KEY'] = 'e194fb5513a73312'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) #instance of database

from flaskblog import routes