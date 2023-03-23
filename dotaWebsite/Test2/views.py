from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from .models import Note, User
from .jsonLoader import main_request, get_recentMatches, get_user
#from .auth import auth

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/heroes', methods=['GET', 'POST'])
def heroes():
    return render_template("heroes.html", user=current_user)

@views.route('/blog', methods=['GET', 'POST'])
def blog():
    #if not auth:
    #    return redirect(url_for('views.user'))
    #Figure this out maybe
    
    return render_template("blogpage.html", user=current_user)





@views.route('/playerprofile', methods=['GET', 'POST']) 
#@login_required
def player():
    if request.method == 'POST':
        
        return redirect(url_for("views.player", user=current_user))

    return render_template("playerprofile.html", user=current_user)





@views.route('/userprofile', methods=['GET', 'POST']) 
@login_required
def user():
    return render_template("userprofile.html", user=current_user)

@views.route('/underconstruction', methods=['GET', 'POST'])
def uc():
    return render_template("underconstruction.html", user=current_user)

@views.route('/match', methods=['GET', 'POST'])
def match():
    return render_template("matchinfo.html", user=current_user)

@views.route('/base', methods=['GET', 'POST'])
def base():
    return render_template("base.html", user=current_user)