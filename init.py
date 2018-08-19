from flask import Flask, flash, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/is-betting-legal-in-us/')
def is_betting_legal():
    return render_template("is-betting-legal-in-us.html")


@app.route('/betting-promotions/')
def betting_promotions():
    return render_template("betting-promotions.html")


@app.route('/betting-bonus')
def betting_bonus():
    return render_template("betting-bonus.html")


@app.route('/no-deposit-bonus/')
def no_deposit_bonus():
    return render_template("no-deposit-bonus.html")


@app.route('/nfl-betitng/')
def nfl_betting():
    return render_template("nfl-betting.html")


@app.route('/about-us/')
def about_us():
    return render_template("about-us.html")


@app.route("/top-rated-betting-sites/")
def top_rated_betting_sites():
    return render_template("top-rated-betting-sites.html")


@app.route("/draftkings/")
def draftkings():
    return render_template("draftkings.html")


@app.route("/bovada/")
def bovada():
    return render_template("bovada.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
