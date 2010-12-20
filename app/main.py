import utils
import glob
import models
import mimetypes
from flask import Flask
from flask import request
from flask import render_template 
from flask import url_for
from flask import redirect
from flask import make_response 
from google.appengine.api import users
 

application = Flask(__name__)

@application.route("/css")
def css():
    scripts = glob.glob("static/css/*.css")
    scripts = sorted(scripts, key=lambda x: x.split("static/css")[1][0])
    return "\n".join(map(utils.get_file_content, scripts))

@application.route("/js")
def js():
    scripts = glob.glob("static/js/*.js")
    scripts = sorted(scripts, key=lambda x: x.split("static/js")[1][0])
    return "\n".join(map(utils.get_file_content, scripts))

@application.route("/img/<image>")
def img(image):
    filename = "static/img/%s" % image
    response = make_response(utils.get_file_content(filename))
    mime = mimetypes.guess_type(filename)
    response.headers["Content-Type"] = mime
    return response

@application.route("/")
def main():
    return render_template("main.html")
