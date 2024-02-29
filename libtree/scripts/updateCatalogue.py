
import csv

import flaskr.controllers.queries.cache as cache


items = cache.getCatalogue()
itemsBuffer = []
for item, tags in items:
    itemsBuffer.append((item, "|".join(tags)))


try:
    fp = open("data/load/cache.csv", "x", encoding="utf-8", newline="")
    writer = csv.writer(fp)
    writer.writerow(['item', 'tags'])
    fp.close()
except:
    print("created cache.csv")


with open("data/load/cache.csv", "a", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerows(itemsBuffer)
    print("Cache updated")
    



