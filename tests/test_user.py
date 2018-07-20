import pytest

from origin.database import db
from origin.models import User, Role
from flask import json


def test_empty_tables(db):
    users = User.query.all()
    assert len(users) == 0
    roles = Role.query.all()
    assert len(roles) == 0


def test_user_creation(db):
    alice = User('alice', 'password')
    db.session.add(alice)
    db.session.commit
    assert User.query.first().username == 'alice'


def test_role_creation(db):
    admin = Role('admin')
    db.session.add(admin)
    db.session.commit
    assert Role.query.first().name == 'admin'


def test_role_allocation(db):
    alice = User('alice', 'password')
    admin = Role('admin')
    editor = Role('editor')
    alice.roles = [admin, editor]
    db.session.add(alice)
    db.session.commit()

    alice = User.query.filter_by(username='alice').one()
    assert len(alice.roles) == 2
    admin = Role.query.filter_by(name='admin').first()
    assert len([admin.users]) == 1
    assert admin.users[0] == alice