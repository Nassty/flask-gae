from google.appengine.api import users
import models
from flask import render_template 
from flask import json

def get_file_content(filename):
    handler = open(filename)
    data = handler.read()
    handler.close()
    return data

def get_login():
    user = users.get_current_user()
    if user:
        url = ("logout (%s)" % user.nickname() , users.create_logout_url("/"))
    else:
        url = ("login", users.create_login_url("/up"))
    return url
