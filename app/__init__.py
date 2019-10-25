from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models.redissession import RedisSessionInterface
app = Flask(__name__, template_folder='../templates', static_folder='../')
app.session_interface = RedisSessionInterface()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{host_id}:{paaword}@{host}:{port}/{schema}?charset=utf8"\
    .format(host_id='home_admin', paaword='hdb1234%', host='localhost', port='3306', schema='clack')

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'hihelloanyonghaso'

db = SQLAlchemy(app)

from app.models import *
from app.routes import route_index
