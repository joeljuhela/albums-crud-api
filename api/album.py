from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from .models import db, Album
from .auth_middleware import auth_required

bp = Blueprint('albums', __name__, url_prefix='/albums')


@bp.route('/', methods=['GET'])
@auth_required
def get_albums():
    albums = Album.query.all()
    return jsonify(albums)


@bp.route('/', methods=['POST'])
@auth_required
def submit_album():
    body = request.json

    try:
        album = Album(**body)
    except TypeError:
        return {}, 400
    try:
        db.session.add(album)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {}, 400

    return jsonify(album), 201


@bp.route('/<int:id>', methods=['GET'])
@auth_required
def get_album(id):
    album = Album.query.filter(Album.id == id).first()
    if not album:
        return {}, 404
    return jsonify(album)


@bp.route('/<int:id>', methods=['DELETE'])
@auth_required
def delete_album(id):
    album = Album.query.filter(Album.id == id).first()
    if album:
        db.session.delete(album)
        db.session.commit()

    return {}, 204


@bp.route('/<int:id>', methods=['PUT'])
@auth_required
def update_album(id):
    body = request.json

    try:
        update_data = Album(**body)
    except TypeError:
        return {}, 400

    album = Album.query.filter(Album.id == id).one()
    if not album:
        return {}, 404
    
    album.title = update_data.title
    album.artist = update_data.artist
    album.release_year = update_data.release_year
    album.genre = update_data.genre
    album.subgenre = update_data.subgenre

    try:
        db.session.commit()
    except IntegrityError:
        return {
            'message': 'Album with same data already exists'
        }, 400
    
    return {}, 200
