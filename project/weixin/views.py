from functools import wraps
from flask import flash, redirect, jsonify, session, url_for, Blueprint, render_template, request

import hashlib
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


@wx_blueprint.route('/weixin')
def weixin_verify():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    
    token = 'testtest' 
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = ''.join(tmplist)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
 
    if hashstr == signature:
         return echostr #success