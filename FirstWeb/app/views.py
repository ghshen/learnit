from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user,logout_user,current_user,login_required
from app import wapp,db,lm,oid
from app.forms import LoginForm
from models import User,ROLE_ADMIN,ROLE_USER
from email import email
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

@wapp.route('/')
@wapp.route('/index')
def index():
    user = g.user
    return render_template('index.html',
                           title = 'Home',
                           user = user)
    
@wapp.route('/login',methods=['GET','POST'])
def login():
    print 'enter login',g.user,g.user.is_authenticated()
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print 'enter validate on submit'
        print form.username.data,form.passwd.data,form.remember_me.data
        session['remember_me' ] = form.remember_me.data
        res = User.query.filter(User.username == form.username.data and User.passwd == form.passwd.data).first()
        print res
        if res is None:
            return render_template('login.html',
                            title = 'Sign In',
                            form = form)
        else:
            remember_me = False
            if 'remember_me' in session:
                remember_me = session['remember_me']
                session.pop('remember_me',None)
            login_user(res, remember=remember_me)
            return redirect(request.args.get('next') )
    else:
        return render_template('login.html',
                            title = 'Sign In',
                            form = form)
    
@lm.user_loader
def load_user(uid):
    return User.query.get(uid)

@wapp.before_request
def before_request():
    g.user = current_user
    
@wapp.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('index'))