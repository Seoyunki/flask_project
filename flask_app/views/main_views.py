import time
from flask import Blueprint, render_template, request, url_for, g
from flask_app.models import Movies, Ratings, Users
from werkzeug.utils import redirect
from ..forms import RatingForm, AddForm
from .. import db
import psycopg2

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('menu/main_menu.html')

@bp.route('/movie/list/')
def movie_list():
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)

    # 영화 목록 전체 쿼리
    movie_list = Movies.query

    # 페이징 구현
    movie_list = movie_list.paginate(page, per_page=10)
    return render_template('movie/movie_list.html', movie_list=movie_list)

@bp.route('/movie/rating/')
def rating_list():
    page = request.args.get('page', type=int, default=1)
    rating_list = Ratings.query.order_by(Ratings.timestamp.desc())
    rating_list = rating_list.paginate(page, per_page=10)
    return render_template('movie/rating_list.html', rating_list=rating_list)

## 평점 등록하기
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = RatingForm()
    if request.method == 'POST':
        db_rating = psycopg2.connect(host='localhost', dbname='s3db', user='postgres', password='seo8009', port=5432)
        cursor = db_rating.cursor()
        cursor.execute("SELECT id from Ratings ORDER BY id desc limit 1")
        result = cursor.fetchone()

        rating = Ratings(id=result[0]+1, userid=form.userid.data, movieid=form.movieid.data, rating=form.rating.data, timestamp=int(time.time()))
        db.session.add(rating)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('movie/rating_form.html', form=form)

## 영화 추가하기
@bp.route('/add/', methods=('GET', 'POST'))
def add():
    form = AddForm()

    if request.method == 'POST':
        db_movie = psycopg2.connect(host='localhost', dbname='s3db', user='postgres', password='seo8009', port=5432)
        cursor = db_movie.cursor()
        cursor.execute("SELECT id from Movies ORDER BY id desc limit 1")
        result = cursor.fetchone()

        movie = Movies(id = result[0] +1, title=form.title.data, genres=form.genres.data)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('movie/add_form.html', form=form)