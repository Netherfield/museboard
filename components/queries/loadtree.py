
import connection
import csv
import utils
import time

query = """INSERT INTO `indexed`(`item_id`, `item`, `category`) VALUES (%s, %s, %s)"""
with open("db/indexed.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    indexes = list(reader)[1:]

    conn = connection.create_db_connection('localhost', 'root', '', 'tree')
    connection.execute_insert(conn, query, indexes)

def loadKeyTree():
    query = """INSERT INTO `keytree` (`branch`, `sub_branch`, `tag`, `category`, `item`, `item_id`) VALUES (%s, %s, %s, %s, %s, %s)"""

    with open("db/keytree.csv", "r", encoding="utf-8", newline="") as fp:
        reader = csv.reader(fp)
        tree = list(reader)[1:]
        prev = 0
        conn = connection.create_db_connection('localhost', 'root', '', 'tree')
        for lines in utils.batch(tree, 10000):
            connection.execute_insert(conn, query, lines)
            br_id = int(lines[-1][1])
            if br_id > prev + 6_000:
                prev = br_id
                conn.close()
                time.sleep(1)
                conn = connection.create_db_connection('localhost', 'root', '', 'tree')
            

print("done")


loadKeyTree()










