from flask import render_template, redirect, url_for, request
from app.models import Movie, Cinema, Schedule, Review
from app import app, db


@app.route("/")
def index():
    return render_template("movies.html")

@app.route('/movies')
def movie_list():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)

@app.route('/schedule')
def schedule_list():
    schedules = Schedule.query.join(Movie).join(Cinema).all()
    return render_template('schedule_list.html', schedules=schedules)


@app.route('/reviews/add', methods=['POST'])
def add_review():
    movie_id = request.form['movie_id']
    rating = request.form['rating']
    comment = request.form.get('comment')
    
    review = Review(movie_id=movie_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('movie_list'))