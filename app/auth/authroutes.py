from flask import Blueprint, render_template, request, redirect, url_for, flash

auth= Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

from .authforms import SignInForm, RegisterForm

# import user, db, and login stuff
from app.models import User,db
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, current_user, logout_user

@auth.route('/', methods=['GET', 'POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':
        if siform.validate_on_submit():
            print(siform.data)
            # check if username entered exists in database and that the passwords match
            user = User.query.filter_by(username=siform.username.data).first()
            # if they dont match, reject and redirect back to sign in , 
            # if they do match, sign user in through login manager
            if user  and check_password_hash(user.password, siform.password.data): # retruns true if psaswords match else will return false
                login_user(user)
                print(current_user, current_user.__dict__)
                flash('You were successfully signed in. Welcome back!')
                return redirect(url_for('home'))
            else:
                flash('Form did not validate. Improper username or password')
                return redirect (url_for('auth.signin'))
        else:
            flash('Form did not validate. Improper username or password')
            return redirect (url_for('auth.signin'))
    return render_template('signin.html', siform=siform)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            newuser = User(rform.username.data, rform.email.data, rform.displayname.data, rform.password.data)
            try: # will produce an error if the username , email, displayname is taken
                db.session.add(newuser)
                db.session.commit()
            except: # if it breaks/doesn't work...
                flash(f'that username,email, or displayname is taken. try something else. ')
                return redirect (url_for('auth.register'))
            login_user(newuser)
            print(rform.data)
            flash(f'Successfully registered. Welcome to our Marvel Family!')
            return redirect(url_for('home'))             
        else:
            flash('Something in your register form isn\'t working. Please try again.')
            return redirect (url_for('auth.register')) 
    return render_template('register.html', rform=rform)

@auth.route('/logout') # only requires get method, which is default so no methods added to decorator line
@login_required
def signout():
    logout_user()
    flash('You have been signed out')
    return redirect(url_for('auth.signin'))