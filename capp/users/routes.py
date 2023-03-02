from flask import render_template, Blueprint, redirect, flash, url_for
from capp.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home.home_home'))
    return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'demo@demo.com' and form.password.data == 'demo':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home.home_home'))
        else:
            flash('Login unsuccessful! Please try again!', 'danger')
    return render_template('users/login.html', title='login', form=form, legend='chapter1')