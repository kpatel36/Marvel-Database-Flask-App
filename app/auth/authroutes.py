from flask import Blueprint, render_template, request, redirect, url_for, flash

auth= Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

from .authforms import SignInForm, RegisterForm

@auth.route('/', methods=['GET', 'POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':
        if siform.validate_on_submit():
            print(siform.data)
            flash('You were successfully signed in. Welcome back!')
            return redirect(url_for('home'))
        else:
            flash('Form did not validate. Improper username or password')
            return redirect (url_for('auth.signin'))
    return render_template('signin.html', siform=siform)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            print(rform.data)
            flash(f'Successfully registered. Welcome to our Marvel Family!')
            return redirect(url_for('home'))
        else:
            flash('Something in your register form isn\'t working. Please try again.')
            return redirect (url_for('auth.register')) 
    return render_template('register.html', rform=rform)