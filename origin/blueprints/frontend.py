from flask import Blueprint, render_template
from flask import current_app as app

bp = Blueprint("frontend", __name__, template_folder="templates", url_prefix="/")


@bp.route("/")
def home():
    return render_template("home.html")
