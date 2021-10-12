from flask import Flask, render_template, url_for
import sqlite3
from mongoLoader import col
import datetime
app = Flask(__name__)

conn = sqlite3.connect('matches.db', check_same_thread=False)
c = conn.cursor()

@app.route("/")
def index():
    teams = col.distinct("team1")
    return render_template("dashboard.html", data=teams)

@app.route("/teamboard/<team>", methods=['GET', 'POST'])
def board(team):
    data = col.find({"team1": {"$eq": team.replace("_", " ")}}).sort([("team1", 1), ("date", -1)]).limit(4)
    return render_template("teamDashboard.html", data=list(data), team=team.replace("_", " "))

@app.route("/teamboardmore/<team>/<year>")
def moreboard(team, year=2020):
    team = team.replace("_", " ")
    data = col.find({"team1": team, "$expr": { "$eq": [{ "$year": "$date" }, int(year)] }}).sort([("team1", 1), ("date", -1)])
    return render_template("teamDashboardMore.html", team=team.replace("_", " "), year=year, data=list(data))

@app.template_filter()
def datetime_format(date):
    """Convert a date to dd/mm/yyyy format."""
    return datetime.datetime.strftime(date, '%d/%m/%Y')

if __name__ == "__main__":
    # l = loader.Loader()
    # l.main()
    #load data to sqlite db from csv
    app.run(debug=True)