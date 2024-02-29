from flask import Blueprint, jsonify, request
from urllib.parse import urlparse, parse_qs


from flaskr.controllers.queries.api import getBoards, getLink, oldestSibling
from flaskr.controllers.queries.cache import update



board_blueprint = Blueprint("board", __name__)

def url_parser():
    url = request.args.get('url')
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    item = params.get('item', [None])[0]
    path = params.get('path', [None])[0].split('/')
    id = params.get('id')[0]
    print(url)
    return {'item': item, 'path': path[1:], 'id': id}



def get_data(branch:int, **args):
    """
    Retrieve data from branch by branch_id.
    The return value is a list like so:
    ...
    Where branch is the branch_id relative to the tag, and items are the board items
    """
    boardData = getBoards(branch)
    branchLookup = dict()
    for line in boardData:
        br, tag, cat, item, item_id = int(line[2]), line[3], int(line[4]), line[5], int(line[6])
        try:
            branchLookup[br]
            branchLookup[br]['items'] += [(cat, (item, item_id))]
        except:
            branchLookup[br] = dict()
            branchLookup[br]['tag'] = tag
            branchLookup[br]['items'] = [(cat, (item, item_id))]


    ret = branchLookup
    for br in ret:
        "fix this to show boards chosen with a logic"
        ret[br]['items'] = list(dict(branchLookup[br]['items']).values())
    return ret

def get_links(itemLookup:list):
    "For every item in the board, get the links from the indexed database"
    boards = dict()
    for br in itemLookup:
        boards[br] = dict()
        boards[br]['tag'] = itemLookup[br]['tag']
        boards[br]['items'] = []
        for item in itemLookup[br]['items']:
            boards[br]['items'] += [(item[0], getLink(item[1]))]
    return boards

def get_alternative(tags:dict):
    return oldestSibling(tags)


@board_blueprint.route("/api/get_board")
def board_control():
    url = url_parser()
    item = url['item']
    path = url['path']
    # clicked branch
    branch = int(url['id'])
    

    "LOOK AT ME IM NEW, CHECK IF I WORK"
    tags = path.split("/")
    if branch[0] == 'U':
        update(item, tags)
    else:
        print("Check if mongoDB server is running")

    itemLookup = get_data(branch)
    if itemLookup == dict():
        jump = get_alternative(tags)
        itemLookup = get_data(jump)

    itemLinks = get_links(itemLookup)

    print(url)
    print(branch, itemLinks)
    return jsonify(itemLinks)

