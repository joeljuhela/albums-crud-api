import csv 

import click
from sqlalchemy import insert
from flask import Blueprint

from .models import User, Album, db


bp = Blueprint('cli', __name__)

@bp.cli.command('create-user')
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

@bp.cli.command('load-albums')
@click.argument('filename')
def load_initial_kaggle_set(filename):
    """Loads an initial dataset to DB to make testing easier"""
    with open(filename, newline='\n', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = []
        next(reader)
        for row in reader:
            rows.append({
                'release_year': int(row[1]),
                'title': row[2],
                'artist': row[3],
                'genre': None if row[4] == 'None' else row[4],
                'subgenre': None if row[5] == 'None' else row[5]
            })

        db.session.execute(
            insert(Album),
            rows
        )
        db.session.commit()