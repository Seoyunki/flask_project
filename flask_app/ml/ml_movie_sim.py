import pandas as pd
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity

# db에서 테이블 불러오기
conn = sqlite3.connect('data_set.db')
cur = conn.cursor()
cur.execute("SELECT * FROM Movies;")
movie_df = pd.DataFrame(cur.fetchall(), columns=['movie_id','title','genres'])
cur.execute("SELECT * FROM Ratings")
rating_df=  pd.DataFrame(cur.fetchall(), columns=['id', 'user_id', 'movie_id', 'rating', 'timestamp'])

rating_df = rating_df[['user_id', 'movie_id', 'rating']]

# rating table 과 movie table join
rating_movies = pd.merge(rating_df, movie_df, on='movie_id')

# 컬럼을 영화 title 로 피벗수행
rating_matrix = rating_movies.pivot_table('rating', index='user_id', columns='title')
# NaN 은 0으로 변환
rating_matrix = rating_matrix.fillna(0)

# 영화간 유사도 산출 (sklearn 의 cosine_similarity 사용)
rating_matrix_T = rating_matrix.transpose()
item_sim = cosine_similarity(rating_matrix_T, rating_matrix_T)
item_sim_df = pd.DataFrame(data=item_sim, index=rating_matrix.columns, columns=rating_matrix.columns)

## 특정영화 입력하고 유사한 영화 리스트 뽑기
print(item_sim_df["Inception (2010)"].sort_values(ascending=False)[:6])