import pandas as pd
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

class ml_movie_item():
    def data_load(self):
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
        return rating_matrix, item_sim_df

        # 해당 영화와 다른 모든 영화간의 유사도 벡터 적용
    def predict_rating(self, ratings_arr, item_sim_arr):
        ratings_pred = ratings_arr.dot(item_sim_arr) / np.array([np.abs(item_sim_arr).sum(axis=1)])
        return ratings_pred

    # mse 구하기
    def get_mse(self, pred, actual):
        pred = pred[actual.nonzero()].flatten()
        actual = actual[actual.nonzero()].flatten()
        return mean_squared_error(pred, actual)

    # Top-N 유사도를 가지는 영화유사도 벡터만 예측값을 계산하는데 사용
    def predict_rating_topsim(self, rating_arr, item_sim_arr, n=20):
        pred = np.zeros(rating_arr.shape)

        for col in range(rating_arr.shape[1]):
            top_n_items = [np.argsort(item_sim_arr[:, col])[:-n - 1:-1]]
            for row in range(rating_arr.shape[0]):
                pred[row, col] = item_sim_arr[col, :][top_n_items].dot(rating_arr[row, :][top_n_items].T)
                pred[row, col] /= np.sum(np.abs(item_sim_arr[col, :][top_n_items]))
        return pred

    # 사용자가 평점을 준 영화를 제외한 영화 리스트를 반환하는 함수
    def get_unseen_movies(self, rating_matrix, userid):
        user_rating = rating_matrix.loc[userid, :]
        already_seen = user_rating[user_rating > 0].index.tolist()
        movies_list = rating_matrix.columns.tolist()
        unseen_list = [movie for movie in movies_list if movie not in already_seen]
        return unseen_list

    def recomm_movie_by_userid(self, pred_df, userid, unseen_list, top_n=10):
        recomm_movies = pred_df.loc[userid, unseen_list].sort_values(ascending=False)[:top_n]
        return recomm_movies

ml = ml_movie_item()

rating_matrix, item_sim_df = ml.data_load()

ratings_pred = ml.predict_rating(rating_matrix.values, item_sim_df.values)

rating_pred_matrix = pd.DataFrame(data=ratings_pred, index=rating_matrix.index, columns=rating_matrix.columns)

ratings_pred = ml.predict_rating_topsim(rating_matrix.values, item_sim_df.values, n=20)

# 계산된 예측 평점 데이터를 DataFrame 으로 생성
ratings_pred_matrix = pd.DataFrame(data=ratings_pred, index=rating_matrix.index, columns=rating_matrix.columns)

userid = 9
unseen_list = ml.get_unseen_movies(rating_matrix, userid)
recomm_movies = ml.recomm_movie_by_userid(ratings_pred_matrix, userid, unseen_list, top_n=10)
recomm_movies = pd.DataFrame(data=recomm_movies.values, index=recomm_movies.index, columns=['pred_score'])

print(recomm_movies)

