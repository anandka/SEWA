# project/models.py


import datetime

from project import db, bcrypt

class AutoSerialize(object):
    'Mixin for retrieving public fields of model in json-compatible format'
    __public__ = None

    def get_public(self, exclude=(), extra=()):
        "Returns model's PUBLIC data for jsonify"
        data = {}
        keys = self._sa_instance_state.attrs.items()
        public = self.__public__ + extra if self.__public__ else extra
        for k, field in  keys:
            if public and k not in public: continue
            if k in exclude: continue
            value = self._serialize(field.value)
            if value:
                data[k] = value
        return data

    @classmethod
    def _serialize(cls, value, follow_fk=False):
        if type(value) in (datetime, date):
            ret = value.isoformat()
        elif hasattr(value, '__iter__'):
            ret = []
            for v in value:
                ret.append(cls._serialize(v))
        elif AutoSerialize in value.__class__.__bases__:
            ret = value.get_public()
        else:
            ret = value

        return ret

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

    def __init__(self, subcategoryid, subcategory_name):
        self.subcategoryid = subcategoryid
        self.subcategory_name = subcategory_name
        
class User(db.Model):

    __tablename__ = "user"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    area = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    postalcode = db.Column(db.String, nullable=False)
    coordinates = db.Column(db.String, nullable=True)

    def __init__(self, username, postalcode, password, name="",
                 phone="", address="", area="", city="", state="", country="" , coordinates=""):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        #self.password = password
        self.name = name
        self.phone = phone
        self.address = address
        self.area = area
        self.city = city
        self.state = state
        self.postalcode = postalcode
        self.country = country
        self.coordinates = coordinates

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        #return self.id
        return self.userid

    def __repr__(self):
        return '<email {}'.format(self.email)


class Service(db.Model):

    __tablename__ = "service"

    serviceid = db.Column(db.Integer, primary_key=True)
    servicename = db.Column(db.String, nullable=True)
    categoryid = db.Column(db.Integer, nullable=False)
    subcategoryid = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String, nullable=True)
    userid = db.Column(db.String, nullable=True)
    

    def __init__(self, servicename, categoryid, subcategoryid, details, userid="1"):
        
        self.servicename = servicename
        self.categoryid = categoryid
        self.subcategoryid = subcategoryid
        self.details = details
        self.userid = userid
        


class Job(db.Model):

    __tablename__ = "job"

    jobid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=True)
    serviceid = db.Column(db.Integer, nullable=False)

    def __init__(self, title, details, serviceid="1"):
        
        self.title = title
        self.details = details
        self.serviceid = serviceid

class City(db.Model):

    __tablename__ = "city"

    cityid = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String, nullable=False)
    stateid = db.Column(db.Integer, nullable=False)

    def __init__(self, cityid, cityname,stateid):
        self.cityid = cityid
        self.cityname = cityname
        self.stateid = stateid

class State(db.Model):

    __tablename__ = "state"

    stateid = db.Column(db.Integer, primary_key=True)
    statename = db.Column(db.String, nullable=False)
    countryid = db.Column(db.Integer, nullable=False)

    def __init__(self, stateid, statename, countryid):
        self.stateid = stateid
        self.statename = statename
        self.countryid = countryid


class Country(db.Model, AutoSerialize):

    __tablename__ = "country"
    __public__ = ('countryid', 'countryname')

    countryid = db.Column(db.Integer, primary_key=True)
    countryname = db.Column(db.String, nullable=True)

    def __init__(self, countryid, countryname):
        self.countryid = countryid
        self.countryname = countryname

    def __repr__(self):
        return 'countryid {}'.format(self.countryid)

class Area(db.Model):

    __tablename__ = "area"

    areaid = db.Column(db.Integer, primary_key=True)
    areaname = db.Column(db.String, nullable=False)
    cityid = db.Column(db.Integer, nullable=False)

    def __init__(self, areaid, areaname, cityid):
        self.areaid = areaid
        self.areaname = areaname
        self.cityid = cityid


