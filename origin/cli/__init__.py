import click
from flask.cli import AppGroup
from origin.database import db
from flask import current_app
import os
from origin.models import User

core_cli = AppGroup("core")
user_cli = AppGroup("user")
db_cli = AppGroup("db")


@core_cli.command("init")
def app_init():
    # create instance directory if it doesn't already exist:
    if not os.path.exists(current_app.instance_path):
        os.makedirs(current_app.instance_path)
        print("[x] Created instance folder")
    db.create_all()
    print("[x] Created database")
    print("App is ready to launch. Run `flask run` to start a production server.")


@user_cli.command("create")
@click.argument("username")
def user_create(username):
    # Lets check if the user exists already:
    u = User.query.filter_by(username=username).first()
    if u:
        return print("User Already Exists")
    u = User(username=username)
    db.session.add(u)
    db.session.commit()

    return print(f"User {u} created")


@user_cli.command("list")
def user_list_all():
    users = [f"    * {x!r}" for x in User.query.all()]
    return print("\n".join(users))
