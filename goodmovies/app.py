from flask import Flask, render_template, request, redirect, jsonify
from cs50 import SQL

#pname = ""
#sport = ""

app = Flask(__name__)

db = SQL("sqlite:///movies.db");

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")     # Use method POST instead of GET in index.html form to hide name in URL
def search():
    q = request.args.get("q")
    if q:
        movies = db.execute("SELECT * FROM movies WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        movies = []
    return jsonify(movies)


