from flask import Flask

from .config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    from api.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from . import album
    from . import auth
    app.register_blueprint(album.bp)
    app.register_blueprint(auth.bp)

    from . import commands
    app.register_blueprint(commands.bp)

    return app
