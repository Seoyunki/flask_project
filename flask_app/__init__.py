import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix":"ix_%(column_0_label)s",
    "uq":"qu_%(table_name)s_%(column_0_name)s",
    "ck":"ck_%(table_name)s_%(column_0_name)s",
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk":"pk_%(table_name)s"
}


db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    #Blueprint
    from .views import main_views, ml_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(ml_views.bp)

    return app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)