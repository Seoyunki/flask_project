import os

BASE_DIR = os.path.dirname(__file__)

#postgres 사용시
#SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{uri}/{db}'.format(user='postgres', pw='seo8009', uri='localhost', db='s3db')

#sqlite 사용시
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'data_set.db'))

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'