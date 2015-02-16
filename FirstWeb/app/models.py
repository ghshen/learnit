from app import db
import sqlalchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship, backref

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = Column(sqlalchemy.Integer,primary_key = True)
    username = Column(sqlalchemy.String(16),index = True,unique = True)
    passwd = Column(sqlalchemy.String(32))
    email = Column(sqlalchemy.String(32),index = True, unique = True)
    role = Column(sqlalchemy.SmallInteger,default = ROLE_USER)
    posts = relationship('Post', backref = 'author',lazy = 'dynamic')
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User %r>' %(self.username)

class Post(db.Model):
    id = Column(sqlalchemy.Integer,primary_key = True)
    body = Column(sqlalchemy.String(140))
    timestamp = Column(sqlalchemy.DateTime)
    user_id = Column(sqlalchemy.Integer,sqlalchemy.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post %r>'  %(self.body)