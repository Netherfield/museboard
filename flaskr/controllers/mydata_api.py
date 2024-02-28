from flask import Blueprint, jsonify, request
import random
from urllib.parse import urlparse, parse_qs




board_blueprint = Blueprint("board", __name__)

def url_parser():
    url = request.args.get('url')
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    tag = params.get('tag', [None])[0]
    path = params.get('path', [None])[0].split('/')
    return {'tag': tag, 'path': path[1:]}


from queries.api import getBoards
def get_data(branch:int, *args):
    """
    Retrieve data from branch by branch_id.
    The return value is a list like so:
    [ [('tag', 'branch'), ['item1', 'item2', ...], ... ]
    Where branch is the branch_id relative to the tag, and items are the board items
    """
    default = {'random' : True, 'miss' : False}
    boardData = getBoards(branch)
    branchLookup = dict()
    for line in boardData:
        br, tag, item, item_id = int(line[2]), line[3], line[5], int(line[6])
        try:
            branchLookup[br]
            branchLookup[br]['items'] += [item]
        except:
            branchLookup[br] = dict()
            branchLookup[br]['tag'] = tag
            branchLookup[br]['items'] = [item]
    print(branchLookup)

if __name__ == '__main__':
    get_data(1)



@board_blueprint.route("/api/get_board")
def board_control():
    url = url_parser()
    tag = url['tag']
    path = url['path']

    """
    SELECT FROM table WHERE tag or path..
    """
    print(tag, path)
    # linzetta = get_data(branch)
    linzetta = [10, []], [11, []], [12, []], [13, []]
    for x in range(len(linzetta)):
        for _ in range(4):
            a = str(random.randint(9, 1000))
            s = "topic" + a
            linzetta[x][1].append(s)
    return jsonify(linzetta)
