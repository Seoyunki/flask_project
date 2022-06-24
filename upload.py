from flask_app.models import Movies, Ratings, Users
import csv
from flask_app import db

## 처음에 데이터 파일 불러오고 LOCAL 서버에 업로드시에만 1회 사용
python3
# # 영화 정보 입력
# f = open('movies_mini.csv', 'r', encoding='utf-8')
# movie_list = csv.reader(f)
# next(movie_list)
#
# for movie in movie_list:
#     m = Movies(title=movie[1], genre=movie[2])
#     db.session.add(m)
# db.session.commit()
#
# # 평점 정보 입력
# f = open('ratings_mini.csv', 'r', encoding='utf-8')
# rating_list = csv.reader(f)
# next(rating_list)
#
# for row in rating_list:
#     r = Ratings(user_id=int(row[0]), movie_id=int(row[1]), rating=float(row[2]), timestamp=int(row[3]))
#     db.session.add(r)
#
# db.session.commit()
#
# # 이름 생성 및 정보 입력
# import random
#
# first_name="김이박최정강조윤장임서"
# middle_name="민서예지도하주윤채현정"
# last_name="준윤우원호후서연아은진빈"
#
# def random_name():
#     result=''
#     result += random.choice(first_name)
#     result += random.choice(middle_name)
#     result += random.choice(last_name)
#     return result
#
# names = []
#
# for i in range(610):
#     name = random_name()
#     names.append(name)
#
# for name in names:
#     u = Users(user_name=name)
#     db.session.add(u)
#
# db.session.commit()

