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
from project.models import TemplatesInfo, Category, Service, Country, Job
from project.email import send_email
from project.token import generate_confirmation_token, confirm_token
from project.decorators import check_confirmed
from project import db, bcrypt
from .forms import LoginForm, RegisterForm, ChangePasswordForm,ProviderForm

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
import json
from flask import jsonify
from sqlalchemy import text
import string
import random

#delete
import os
from io import BytesIO
import StringIO
import zipstream
#import MySQLdb

#db = MySQLdb.connect("localhost", "root", "", "sewa")

################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['name']).first()
        print user.password
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            #flash('Welcome.', 'success')
            return render_template('html/myservices.html')
        else:
            #flash('Invalid email and/or password.', 'danger')
            return render_template('html/login.html')
    return render_template('html/login.html')


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



@user_blueprint.route('/home', methods=['GET', 'POST'])
#@login_required
def home():
    return render_template('html/home.html')

@user_blueprint.route('/provider/', methods=['GET', 'POST'])
#@login_required
def provider():
    #return "Welcome to the provider page"
    if request.method == 'POST':
        #form = ProviderForm(request.form)
        service = Service(
        categoryid=request.form['Sname'],
        subcategoryid=request.form['Aname'],
        userid = request.form['Rname'],
        firmname = request.form['Cname']
        )
        db.session.add(service)
        
        db.session.commit()
        return "successfully created"
    return render_template('user/provider.html')

@user_blueprint.route('/seeker/', methods=['GET', 'POST'])
#@login_required
def seeker():
    #return "Welcome to the seeker page"
    return render_template('user/seeker.html')



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


@user_blueprint.route('/search_service', methods=['GET', 'POST'])
def search_service():
    if request.method == 'POST':
        return "there will be db queries in here"
    return render_template('html/search_service.html')

@user_blueprint.route('/search_job', methods=['GET', 'POST'])
def search_job():
    if request.method == 'POST':
        return "there will be db queries in here"
    return render_template('html/search_job.html')

@user_blueprint.route('/dropdown_info/<token>', methods=['GET', 'POST'])
def dropdown_info(token):
    a = '[{"key":"A", "val" : "anand"},{"key":"B", "val" : "Karwa"}]'
    info = Country.query.filter_by().all()
    ret = "{"
    
    for i in info:
        #ret = ret + "key : " + i.countryid + ","
        print (i.countryid)
        print (i.countryname)
    return a

@user_blueprint.route('/testdb')

def test_db():
    #return current_user.email
    #info = TemplatesInfo.query.get(email=current_user.email).all()
    info = Category.query.filter_by(category_name='Plumber').all()
    info = Category.query.all()
    for i in info:
        print(i.categoryid)
        print(i.category_name)
    #query.order_by(User.username)
    #print info.email
    return "done please read your console"


@user_blueprint.route('/uitest')
def test_ui():
    return render_template('user/sample_delete.html')

@user_blueprint.route('/register')
def register_html():
    print "in register_html"
    return render_template('html/register.html')    

@user_blueprint.route('/saveUser', methods=['GET', 'POST'])
def saveUser():
    #username=request.form['name']
    #print username
    if request.method == 'POST':
        user = User(
        username=request.form['name'],
        password=request.form['password'],
        country = request.form['country'],
        area = request.form['area'],
        city = request.form['city'],
        state = request.form['state'],
        phone = request.form['phone'],
        postalcode = request.form['pincode'],
        name = "Dummy",
        address = "add",
        coordinates = "123"
        )
        
        db.session.add(user)
        db.session.commit()
        print"user successfully saved"
        return render_template('html/myservices.html')
    return render_template('html/userhome.html')

@user_blueprint.route('/edituser', methods=['GET', 'POST'])
def edituser():
    return render_template('html/edituser.html')

@user_blueprint.route('/myservices', methods=['GET', 'POST'])
def myservices():
    return render_template('html/myservices.html')

@user_blueprint.route('/myjobs', methods=['GET', 'POST'])
def myjobs():
    return render_template('html/myjobs.html')

@user_blueprint.route('/addjob', methods=['GET', 'POST'])
def addjob():
    if request.method == 'POST':
        print "success"
        job = Job(
            title=request.form['title'],
            details=request.form['details'],
            serviceid=request.form['serviceid']
            )
        db.session.add(job)
        db.session.commit()

        return render_template('html/myjobs.html')
    return render_template('html/AddJob.html')

@user_blueprint.route('/addservice', methods=['GET', 'POST'])
def addservice():
    if request.method == 'POST':
        service = Service(
             servicename=request.form['servicename'],
             categoryid=request.form['categoryid'],
             subcategoryid=request.form['subcategoryid'],
             details=request.form['details'],
             userid=current_user.userid
             )
        db.session.add(service)
        db.session.commit()

        return render_template('html/myservices.html')
    return render_template('html/AddService.html')



@user_blueprint.route('/smsregister/<phone>/<pincode>')
def smsregister(phone, pincode):
    password = id_generator()
    smsuser = User(
        username=phone,
        postalcode=pincode,
        password=password
    )
    db.session.add(smsuser)
    db.session.commit()

    return "success " + password

@user_blueprint.route('/searchservice', methods=['GET','POST'])
def searchservice():
    if request.method == 'POST':
        sql = text('select s.serviceid,s.servicename,c.category_name ,subc.subcategory_name, s.details from service s  inner join category c on c.categoryid = s.categoryid inner join subcategory subc on subc.subcategoryid = s.subcategoryid  and subc.categoryid=c.categoryid where userid = '+str(current_user.userid)+';')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"servicename" : "' +str(row.servicename) + '", "categoryname":"' +str(row.category_name) + '", "subcategoryname":"' + str(row.subcategory_name) + '","details":"' + str(row.details) +'"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        print res_json
        return res_json
    return "success"


@user_blueprint.route('/searchjob', methods=['GET','POST'])
def searchjob():
    if request.method == 'POST':
        #countryid = request.form['countryid']
        #stateid = request.form['stateid']
        #cityid = request.form['cityid']
        #areaid = request.form['areaid']
        #categoryid = request.form['categoryid']
        #subcategoryid = request.form['subcategoryid']
        #print "\n\n\n\n\n"
        #print subcategoryid
        #print areaid
        sql = text('select j.jobid,j.title ,j.details,s.servicename from job j inner join service s on s.serviceid=j.serviceid where s.userid= '+str(current_user.userid)+';')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"servicename" : "' +str(row.servicename) + '", "title":"' +str(row.title) + '", "details":"' + str(row.details) + '"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        return res_json
    return "success"

@user_blueprint.route('/dropdowncategory', methods=['GET','POST'])
def dropdowncategory():
    if request.method == 'POST':
        sql = text('select * from category;')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"key" : "' +str(row.categoryid) + '", "val":"' +str(row.category_name)+'"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        return res_json

@user_blueprint.route('/dropdownsubcategory/<categoryid>', methods=['GET','POST'])
def dropdownsubcategory(categoryid):
    if request.method == 'POST':
        sql = text('select * from subcategory where categoryid = '+categoryid+';')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"key" : "' +str(row.subcategoryid) + '", "val":"' +str(row.subcategory_name)+'"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        return res_json

@user_blueprint.route('/userservice', methods=['GET','POST'])
def userservice():
    if request.method == 'POST':
        sql = text('select serviceid, servicename from service where userid = '+str(current_user.userid)+';')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"key" : "' +str(row.serviceid) + '", "val":"' +str(row.servicename)+'"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        print res_json
        return res_json

@user_blueprint.route('/dropdowncountry', methods=['GET','POST'])
def dropdowncountry():
    if request.method == 'POST':
        sql = text('select * from country;')
        res_json = "["
        result = db.engine.execute(sql)
        for row in result:
            res_json =  res_json + '{"key" : "' +str(row.countryid) + '", "val":"' +str(row.countryname)+'"},'
        res_json =res_json[:-1]
        res_json = res_json + "]"
        print res_json
        return res_json