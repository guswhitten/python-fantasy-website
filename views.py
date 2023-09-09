from flask import Blueprint, render_template, request
from espn_api import football
from get_league_data import create_chart_race

views = Blueprint(__name__, "views")

@views.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html", display = False, displayLeagueInfo = False)

@views.route("/fantasy", methods=["GET", "POST"])
def fantasy():
    if request.method == "POST":
        league_id = request.form.get("id")
        year = request.form.get("year")
        league = football.League(league_id=int(league_id), year=int(year))
        return render_template("index.html", display = False, displayLeagueInfo = True, league=league)
    else:
        return render_template("index.html", display = False, displayLeagueInfo = False)
    

@views.route("/bar_chart_race", methods=["GET", "POST"])
def bar_chart_race():
    display = False
    if request.method == "POST":
        league_id = request.form.get("id")
        year = request.form.get("year")
        league = football.League(league_id=int(league_id), year=int(year))
        create_chart_race(league)
        display = True
        return render_template("index.html", display=display, len=len(league.teams))
    else:
        return render_template("index.html", display = False, displayLeagueInfo = False)