from flask import Blueprint, render_template, request
from espn_api import football
from get_league_data import create_chart_race

views = Blueprint(__name__, "views")


@views.route("/home")
@views.route("/")
def home_page():
    return render_template("index.html")


@views.route("/projects")
def projects():
    return render_template("projects.html")


@views.route("/arcade")
def arcade():
    return render_template("arcade.html")


@views.route("/fantasy", methods=["GET", "POST"])
def fantasy():
    display = False
    if request.method == "POST":
        league_id = request.form.get("id")
        year = request.form.get("year")
        league = football.League(league_id=int(league_id), year=int(year))
        create_chart_race(league)
        display = True
        return render_template("fantasy.html", display=display, len=len(league.teams))
    else:
        return render_template("fantasy.html")
