from flask_app import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    genres = db.Column(db.String(200))

class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    movieid = db.Column(db.Integer, db.ForeignKey('movies.id', ondelete='CASCADE'), nullable=False)
    rating = db.Column(db.Float)
    timestamp = db.Column(db.Integer)
    user = db.relationship('Users', backref=db.backref('user_set'))
    movie = db.relationship('Movies', backref=db.backref('movie_set'))

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)

class Suggests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    suggest_movie = db.Column(db.String(200))
    suggest_time = db.Column(db.Integer)