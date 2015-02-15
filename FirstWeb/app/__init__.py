import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from app.config import basedir

wapp = Flask(__name__)
wapp.config.from_object('config')
db = SQLAlchemy(wapp)
lm = LoginManager()
lm.init_app(wapp)
lm.login_view= 'login'
oid = OpenID(wapp,os.path.join(basedir,'tmp'))

from app import views,models
