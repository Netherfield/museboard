
try:
    import flaskr.controllers.queries.connection as connection
except:
    import connection



def getBoards(branch_id:int, hit=False) -> list[tuple[int,int,int,str,int,str,int]]:
    """Queries the database for branch_id
    if hit is set to True keeps decreasing branch_id
    until it hits a result
    
    returns a list:
    
    [(auto_id, branch, sub_branch, tag, category, item, item_id), ...]

    'auto_id' is the sql primary key
    'branch' and 'sub_branch' are branch ids
    'tag' is the sub_branch tag
    'category' is a number identifying the source dataset
    'item' is the name of the item
    'item_id' is the id of the item in relation to the 'indexed' table

    """
    query = f"""SELECT *
                FROM keytree
                WHERE branch = {branch_id};"""
    conn = connection.create_db_connection('localhost', 'root', '', 'tree')
    boards = connection.read_query(conn, query)
    if boards == [] and hit:
        return getBoards(branch_id - 1, True)
    return boards


def getLink(item_id:int):
    query = f"""SELECT item_id
                FROM indexed
                WHERE item_id = {item_id};"""
    conn = connection.create_db_connection('localhost', 'root', '', 'tree')
    try:
        link = connection.read_query(conn, query)
    except:
        link = "no_link"

    return link[0][0]



"""TODO:
implement:
- getUnindexed: queries the unindexed list for random(?) items
- getUnlimited: queries a far off branch to keep retrieving boards and/or queries the unindexed
"""

