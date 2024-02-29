import csv

import splicer

items_path = "reports/items.csv"
items_lines = sum(1 for _ in open(items_path, "r", encoding="utf-8"))



with open(items_path, "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()

    allTags = dict()
    for chunk in splicer.readChunk(reader, 1000):
        
        rTags = []
        for line in chunk:
            # non repeating per single item
            rTags += list(set(line[1].split("|")))

    
        index = list(set(rTags))
        countTags = { t : 0 for t in index}
        for tag in rTags:
            countTags[tag] += 1

        for key in countTags:
            c = countTags[key]
            try:
                allTags[key] += c
            except:
                allTags[key] = c


tags = list(allTags.items())
tags.sort(key=lambda a: int(a[1]), reverse=True)

with open("reports/tags.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(['tag', 'count'])
    writer.writerows(tags)








