# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask.ext.login import login_required
from project.decorators import check_confirmed


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################

@main_blueprint.route('/')

def home():
    return render_template('user/welcome.html')
