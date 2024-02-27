from flask import Blueprint, jsonify, request
from urllib.parse import urlparse, parse_qs
import random

color_blueprint = Blueprint("color", __name__)


@color_blueprint.route("/api/get_color")
def color_control():
    colors = [
        "red", "blue", "green", "yellow", "purple",
        "cyan", "magenta", "black", "gray",
        "orange", "pink", "violet", "indigo", "gold",
        "silver", "brown", "teal", "navy", "maroon"
    ]
    new_color = random.choice(colors)
    return jsonify(new_color)


