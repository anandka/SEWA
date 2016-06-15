# project/user/views.py


#################
#### imports ####
#################
import datetime
from project.email import send_email
from project.decorators import check_confirmed


from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, make_response, send_file
from flask.ext.login import login_user, logout_user, \
    login_required, current_user
from project.token import generate_confirmation_token, confirm_token

from project.models import User
from project.models import TemplatesInfo
from project.email import send_email
from project.token import generate_confirmation_token, confirm_token
from project.decorators import check_confirmed
from project import db, bcrypt
from .forms import LoginForm, RegisterForm, ChangePasswordForm

from flask import current_app
import os
#from flask import Flask, redirect, url_for, request, render_template
from werkzeug import secure_filename
import zipfile
from flask import Response
import uuid
import time
import glob
import config

#delete
import os
from io import BytesIO
import StringIO
import zipstream


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    print"I am in register"
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=form.password.data,
            confirmed=False
        )
        db.session.add(user)
        db.session.commit()


        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)

        flash('A confirmation email has been sent via email.', 'success')
        #return redirect(url_for("main.home"))
        return redirect(url_for("user.unconfirmed"))


    return render_template('user/register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.', 'success')
    return redirect(url_for('user.login'))


@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
@check_confirmed
def profile():
    form = ChangePasswordForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Password successfully changed.', 'success')
            return redirect(url_for('user.profile'))
        else:
            flash('Password change was unsuccessful.', 'danger')
            return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form=form)


@user_blueprint.route('/confirm/<token>')
@login_required
def confirm_email(token):
    if current_user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
        return redirect(url_for('main.home'))
    email = confirm_token(token, expiration=3600)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    if user.email == email:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'danger')
    return redirect(url_for('main.home'))


@user_blueprint.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('main.home'))
    flash('Please confirm your account!', 'warning')
    return render_template('user/unconfirmed.html')


@user_blueprint.route('/homepage/', methods=['GET', 'POST'])
#@login_required
def input():
    return render_template('user/welcome.html')

@user_blueprint.route('/provider/', methods=['GET', 'POST'])
#@login_required
def ip():
    return "Welcome to the provider page"



@user_blueprint.route('/resend')
@login_required
def resend_confirmation():
    print "in resend"
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('user.confirm_email', token=token, _external=True)
    html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    print "\n\n\n\n"+ current_user.email
    print "\n" + subject
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    print "\n\n\n\n"
    return redirect(url_for('user.unconfirmed'))


@user_blueprint.route('/testdb')
@login_required
def test_db():
    data = current_user.email
    #return current_user.email
    #info = TemplatesInfo.query.get(email=current_user.email).all()
    info = TemplatesInfo.query.filter_by(template_name='Orders.txt_2016-05-25 18:48:18.533653').all()
    info = TemplatesInfo.query.all()
    for i in info:
        print(i.email)
    #query.order_by(User.username)
    #print info.email
    return  "you are awesome"
