from functools import wraps
from flask import flash, redirect, jsonify, session, url_for, Blueprint, render_template, request

import hashlib
from project import db
from project.models import Task

import lxml
import time
import os
import urllib2,json
from lxml import etree

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

@wx_blueprint.route('/weixin', methods=['POST'])
def weixin_echo_you_said():
    str_xml = request.data()
    xml = etree.fromstring(str_xml)
    content = xml.find("Content").text
    msg_type = xml.find("MsgType").text
    from_user = xml.find("FromUserName").text
    to_user = xml.find("ToUserName").text
    return render_template('reply_text.xml',from_user=from_user, 
        to_user=to_user, create_time=int(time.time()), content='current just test, what you said is {}'.format(content))









