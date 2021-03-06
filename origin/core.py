from werkzeug.utils import find_modules, import_string
from flask import Flask
from .database import db
from .cli import core_cli, db_cli, user_cli
from .models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore


def create_app(config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="default",
        SQLALCHEMY_DATABASE_URI="postgresql://localhost/project",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # app.config.from_object('origin.settings')
    app.config.from_pyfile("settings.cfg", silent=True)
    if config:
        app.config.from_pyfile(config)

    register_database(app)
    register_security(app)
    register_cli(app)
    register_blueprints(app)
    return app


def register_security(app):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security()
    security.init_app(app, user_datastore)
    return None


def register_database(app):
    db.init_app(app)
    return None


def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules("origin.blueprints"):
        mod = import_string(name)
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    app.cli.add_command(db_cli)
    app.cli.add_command(core_cli)
    app.cli.add_command(user_cli)
