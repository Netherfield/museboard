from flask import Blueprint, request, jsonify
from urllib.parse import urlparse, parse_qs
import random

board_blueprint = Blueprint("board", __name__)

@board_blueprint.route("/api/get_board")
def board_control():
    # url = request.args.get('url')
    # parsed_url = urlparse(url)
    # params = parse_qs(parsed_url.query)
    # tag = params.get('tag', [None])[0]
    # path = params.get('path', [None])[0].split('/')
    # print('tag: ', tag, 'path: ', path[1:])
    def get_data(arg=None):
        """
        Get Board Data -> ][1, [1,2,3,4]], [2, [1,2,3,4]], ...]
        :return:
        """
        if arg:
            # GET DATA
            pass
    linzetta = [10, []], [11, []], [12, []], [13, []]
    for x in range(len(linzetta)):
        for _ in range(4):
            a = str(random.randint(9, 1000))
            s = "topic" + a
            linzetta[x][1].append(s)
    return jsonify(linzetta)
