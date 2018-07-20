import os
import pytest
import inspect


from origin.core import create_app
from origin.database import db as _db


@pytest.yield_fixture(scope="session")
def app():
    """Session-wide test `Flask` application"""
    app = create_app(config='test_settings.cfg')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope="session")
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope="function", autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()
