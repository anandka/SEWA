# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, email, password, confirmed,
                 admin=False, confirmed_on=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

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
