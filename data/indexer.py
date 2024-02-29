

"""TODO: create list of indexed and non indexed items, add the id to the csv"""

import csv

i = 0
catItems = dict()
catTree = dict()
while(True):
    try:
        i += 1
        fp = open("drop/items" + str(i) + '.csv', "r", encoding="utf-8")
        reader = csv.reader(fp)
        reader.__next__()
        catItems[i] = list(reader)
        catTree[i] = []
    except:
        if i > 10:
            break



with open("db/tree.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()
    for line in reader:
        cat = int(line[3])
        catTree[cat] += [line[4]]


indexed = []
unindexed = []
for cat in catTree:
    from itertools import product
    ind = set(catTree[cat])
    und = list(set(dict(catItems[cat]).keys()) - ind)
    und = product(und, range(cat, cat+1))
    unindexed += und

    ind = list(ind)
    ind = product(ind, range(cat, cat+1))
    indexed += ind
   

with open("indexed.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(['item_id', 'item', 'category'])
    for i in range(1, len(indexed) + 1):
        writer.writerow([i,*indexed[i-1]])

with open("unindexed.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(['item_id', 'item', 'category'])
    for i in range(1, len(unindexed) + 1):
        writer.writerow([i,*unindexed[i-1]])


