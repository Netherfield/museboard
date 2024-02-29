
import csv


indices = dict()
with open("db/indexed.csv", "r", encoding="utf-8", newline="") as fread:
    indexReader = csv.reader(fread)
    indexReader.__next__()
    for id, name, _ in indexReader:
        indices[name] = id
        

fwrite = open("db/keytree.csv", "w", encoding="utf-8", newline="")
keytreeWriter = csv.writer(fwrite)
with open("db/tree.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()
    keytreeWriter.writerow(['br_id', 'subbr_id', 'tag', 'category', 'item', 'item_id'])
    for *args, item in reader:
        try:
            item_id = indices[item]
        except:
            print('error')
            exit()
        keytreeWriter.writerow([*args, item, item_id])

fwrite.close()

