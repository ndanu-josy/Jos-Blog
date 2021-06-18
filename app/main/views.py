from flask import render_template,request,redirect,url_for,flash
from . import main
from .. import db,photos
from flask_login import login_user,logout_user,login_required,current_user
from ..requests import getQuotes
from .forms import BlogForm,CommentForm,updateProfile
from ..models import Blog,Comment,User

@main.route('/',methods = ['GET'])
def index():
    getquotes = getQuotes()
    return render_template ('index.html',getquotes = getquotes)

