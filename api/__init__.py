import os
import mariadb
import click
import json

from flask import Flask
from sqlalchemy.exc import IntegrityError

from .models import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mariadb+mariadbconnector://root:test@db/test'
    )

    from api.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import album
    from . import auth
    app.register_blueprint(album.bp)
    app.register_blueprint(auth.bp)

    @app.cli.command('create-user')
    @click.option('--username', prompt=True)
    @click.password_option()
    def create_user(username, password):
        user = User(
            username=username
        )
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            click.echo('User with that password already exists!')

    
    return app