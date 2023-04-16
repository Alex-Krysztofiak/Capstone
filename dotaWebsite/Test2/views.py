from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from .models import Note, User
from .player_loader import Player
#from .auth import auth
from pprint import pprint

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/heroes', methods=['GET', 'POST'])
@login_required
def heroes():
    # This will redirect on searchbar
    if request.form.get("playerid"):
        player_id = request.form.get("playerid")
        return redirect(url_for('views.player', number = player_id))

    return render_template("heroes.html", user=current_user)

@views.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    # This will redirect on searchbar
    if request.form.get("playerid"):
        player_id = request.form.get("playerid")
        return redirect(url_for('views.player', number = player_id))
    
    return render_template("blogpage.html", user=current_user)

@views.route('/player_<number>', methods=['GET', 'POST']) 
@login_required
def player(number): 
    num = Player(number)
    num.display_player()

    # This will redirect on searchbar
    if request.form.get("playerid"):
        player_id = request.form.get("playerid")
        return redirect(url_for('views.player', number = player_id))
    
    return render_template("playerprofile.html", user=current_user)

@views.route('/match', methods=['GET', 'POST'])
@login_required
def match():
    # This will redirect on searchbar
    if request.form.get("playerid"):
        player_id = request.form.get("playerid")
        return redirect(url_for('views.player', number = player_id))
    # if request.method == 'POST':
    #     match_id = request.form.get("matchid-btn")
    #     print(match_id)
    #     # return redirect(url_for("match.user", user=current_user))
    return render_template("match.html", user=current_user)
  

@views.route('/base', methods=['GET', 'POST'])
@login_required
def base():
    return render_template("base.html", user=current_user)

# @views.route('/underconstruction', methods=['GET', 'POST'])
# def uc():
#     return render_template("underconstruction.html", user=current_user)