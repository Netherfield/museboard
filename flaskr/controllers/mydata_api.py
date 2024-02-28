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
            branchLookup[br]['items'] = [(cat, item)]

    ret = branchLookup
    for br in ret:
        branchLookup[br]['items'] = list(dict(branchLookup[br]['items']).values())
    
    

    for br in ret:
        print(br)
        for key in ret[br]:
            print(key, ret[br][key])

if __name__ == '__main__':
    get_data(1)



@board_blueprint.route("/api/get_board")
def board_control():
    url = url_parser()
    tag = url['tag']
    path = url['path']
    # clicked branch
    branch = url['branch']
    jump = False
    print(tag, path)

    # if len(path.split("/")) % 5 == 0:
    #     jump = True

    linzetta = get_data(branch, jump)
    linzetta = [10, []], [11, []], [12, []], [13, []]
    for x in range(len(linzetta)):
        for _ in range(4):
            a = str(random.randint(9, 1000))
            s = "topic" + a
            linzetta[x][1].append(s)
    return jsonify(linzetta)
