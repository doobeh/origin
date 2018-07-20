from flask import Blueprint
from random import randint
from flask import jsonify

bp = Blueprint("api", __name__, template_folder="templates", url_prefix="/api")


@bp.route("/d6")
def dice_roll():
    return jsonify(dice_roll=randint(1, 6))
