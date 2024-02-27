from flask import Blueprint, request, jsonify
from urllib.parse import urlparse, parse_qs
import random

board_blueprint = Blueprint("board", __name__)


def get_data():
    """
    Get Board Data -> ][1, [1,2,3,4]], [2, [1,2,3,4]], ...]
    :return:
    """
    pass

def url_parser():
    url = request.args.get('url')
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    tag = params.get('tag', [None])[0]
    path = params.get('path', [None])[0].split('/')
    return {'tag': tag, 'path': path[1:]}


@board_blueprint.route("/api/get_board")
def board_control():
    url = url_parser()
    tag = url['tag']
    path = url['path']
    """
    SELECT FROM table WHERE tag or path..
    """
    print(tag, path)
    # linzetta = get_data()
    linzetta = [10, []], [11, []], [12, []], [13, []]
    for x in range(len(linzetta)):
        for _ in range(4):
            a = str(random.randint(9, 1000))
            s = "topic" + a
            linzetta[x][1].append(s)
    return jsonify(linzetta)
