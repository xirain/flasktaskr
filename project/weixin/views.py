from functools import wraps
from flask import flash, redirect, jsonify, session, url_for, Blueprint, render_template

from project import db
from project.models import Task

################
#### config ####
################

wx_blueprint = Blueprint('wx', __name__)

#####################
###### routes #######
#####################

@wx_blueprint.route('/wx/test/')

def wx_test():
    return render_template('test.html')