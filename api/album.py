from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import IntegrityError

from .models import db, Album

bp = Blueprint('albums', __name__, url_prefix='/albums')

@bp.route('/', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    return jsonify(albums)

@bp.route('/', methods=['POST'])
def submit_album():
    body = request.json

    try:
        album = Album(**body)
    except TypeError as e:
        return jsonify({}), 400
    try:
        db.session.add(album)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({}), 400
    
    return jsonify(album), 201, {'location': f'/{album.id}'}


@bp.route('/<int:id>', methods=['GET'])
def get_album(id):
    album = Album.query.filter(Album.id == id).one()
    if not album:
        return 404
    else:
        return jsonify(album)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_album(id):
    pass

@bp.route('/<int:id>', methods=['PUT'])
def update_album(id):
    pass