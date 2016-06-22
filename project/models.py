# project/models.py


import datetime

from project import db, bcrypt



class TemplatesInfo(db.Model):

    __tablename__ = "templates_info"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    template_name = db.Column(db.String, nullable=False)
    token = db.Column(db.String) # do nullable=False
    timestamp = db.Column(db.String) # do nullable=False
    template_status = db.Column(db.String)

    def __init__(self, email, template_name, template_status, token, timestamp):
        self.email = email
        self.template_name = template_name
        self.template_status = template_status
        self.token = token
        self.timestamp = timestamp
        #self.registered_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    #def __repr__(self):
    #    return 'email {}'.format(self.email)
    #def __repr__(self):
    #    return 'email: %s template_status: %s' % (self.email, self.template_status)
            #self.email.encode('utf8'), self.template_status.encode('utf8'))

class Category(db.Model):

    __tablename__ = "category"

    categoryid = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, nullable=True)

    def __init__(self, category_name):
        self.category_name = category_name

class SubCategory(db.Model):

    __tablename__ = "subcategory"

    subcategoryid = db.Column(db.Integer, primary_key=True)
    subcategory_name = db.Column(db.String, nullable=True)
    categoryid = db.Column(db.Integer, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name
        
class User(db.Model):

    __tablename__ = "user"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    area = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    postalcode = db.Column(db.String, nullable=True)

    def __init__(self, username, password, name,
                 phone, address, area, city, state, postalcode):
        self.username = username
        #self.password = bcrypt.generate_password_hash(password)
        self.password = password
        self.name = name
        self.phone = phone
        self.address = address
        self.area = area
        self.city = city
        self.state = state
        self.postalcode = postalcode

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<email {}'.format(self.email)


class Service(db.Model):

    __tablename__ = "service"

    serviceid = db.Column(db.Integer, primary_key=True)
    categoryid = db.Column(db.Integer, nullable=False)
    subcategoryid = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.String, nullable=True)
    firmname = db.Column(db.String, nullable=True)

    def __init__(self, categoryid, subcategoryid, userid, firmname):
        self.categoryid = categoryid
        self.subcategoryid = subcategoryid
        self.userid = userid
        self.firmname = firmname


class Job(db.Model):

    __tablename__ = "job"

    jobid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=True)
    serviceid = db.Column(db.Integer, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name

class City(db.Model):

    __tablename__ = "city"

    cityid = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String, nullable=False)
    stateid = db.Column(db.Integer, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name

class State(db.Model):

    __tablename__ = "state"

    stateid = db.Column(db.Integer, primary_key=True)
    statename = db.Column(db.String, nullable=False)
    countryid = db.Column(db.Integer, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name


class Country(db.Model):

    __tablename__ = "country"

    countryid = db.Column(db.Integer, primary_key=True)
    countryname = db.Column(db.String, nullable=True)

    def __init__(self, category_name):
        self.category_name = category_name

class Area(db.Model):

    __tablename__ = "area"

    areaid = db.Column(db.Integer, primary_key=True)
    areaname = db.Column(db.String, nullable=False)
    cityid = db.Column(db.Integer, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name
