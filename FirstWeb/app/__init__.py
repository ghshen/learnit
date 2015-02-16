import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from app.config import basedir,SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

wapp = Flask(__name__)
wapp.config.from_object('config')

db = SQLAlchemy(wapp)
engine = create_engine(SQLALCHEMY_DATABASE_URI,echo = True,pool_size = 20,max_overflow = 0)
Session = sessionmaker(bind = engine)
dbsession = Session()

lm = LoginManager()
lm.init_app(wapp)
lm.login_view= 'login'
oid = OpenID(wapp,os.path.join(basedir,'tmp'))

from app import views,models
