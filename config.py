import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{uri}/{db}'.format(user='postgres', pw='seo8009', uri='localhost', db='s3db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'