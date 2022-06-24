from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired

class RatingForm(FlaskForm):
    userid = IntegerField('유저ID', validators=[DataRequired()])
    movieid = IntegerField('영화ID', validators=[DataRequired()])
    rating = FloatField('평점', validators=[DataRequired()])

class AddForm(FlaskForm):
    title = StringField('영화제목', validators=[DataRequired()])
    genres = StringField('장르', validators=[DataRequired()])

class mlForm(FlaskForm):
    title = IntegerField('사용자ID', validators=[DataRequired()])

class mlsubForm(FlaskForm):
    movie_title = StringField('영화제목', validators=[DataRequired()])