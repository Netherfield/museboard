from flask import Blueprint, jsonify, request
from urllib.parse import urlparse, parse_qs




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


from flaskr.controllers.queries.api import getBoards, getLink
def get_data(branch:int, **args):
    """
    Retrieve data from branch by branch_id.
    The return value is a list like so:
    [ [('tag', 'branch'), ['item1', 'item2', ...], ... ]
    Where branch is the branch_id relative to the tag, and items are the board items
    """
    default = {'rand' : True, 'miss' : False, 'jump' : False, 'reset' : False}
 

    # if jump:
    #     branch %= 100
    boardData = getBoards(branch)
    branchLookup = dict()
    for line in boardData:
        br, tag, cat, item, item_id = int(line[2]), line[3], int(line[4]), line[5], int(line[6])
        try:
            branchLookup[br]
            branchLookup[br]['items'] += [(cat, item)]
        except:
            branchLookup[br] = dict()
            branchLookup[br]['tag'] = tag
            branchLookup[br]['items'] = [(cat, (item, item_id))]


    ret = branchLookup
    for br in ret:
        "fix this to show boards chosen with a logic"
        ret[br]['items'] = list(dict(branchLookup[br]['items']).values())
        print(ret)
        exit()
    return ret

def get_links(itemLookup:list):
    "For every item in the board, get the links from the indexed database"
    boards = dict()
    for br in itemLookup:
        boards[br] = dict()
        boards[br]['tag'] = itemLookup[br]['tag']
        boards[br]['items'] = []
        for item in itemLookup[br]['items']:
            boards[br]['items'] = (item[0], getLink(item[1]))
        
    return boards


@board_blueprint.route("/api/get_board")
def board_control():
    url = url_parser()
    tag = url['item']
    path = url['path']
    # clicked branch
    branch = int(url['id'])
    # if len(path.split("/")) % 5 == 0:
    #     jump = True
    itemLookup = get_data(branch)

    itemLinks = get_links(itemLookup)
    # linzetta = [10, []], [11, []], [12, []], [13, []]
    # for x in range(len(linzetta)):
    #     for _ in range(4):
    #         a = str(random.randint(9, 1000))
    #         s = "topic" + a
    #         linzetta[x][1].append(s)
    print(url)
    print(branch, itemLinks)
    return jsonify(itemLinks)
