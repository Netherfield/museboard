
import csv

with open("reports/tags.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()
    tags = [(tag, int(count)) for tag, count in reader]

with open("reports/items.csv", "r", encoding="utf-8", newline="") as fp:
    reader =csv.reader(fp)
    reader.__next__()
    itemsLookup = dict([(item, tag.split("|")) for item, tag in reader])


top = 100
top_tags = list(dict(tags[:top]).keys())
rawCluster = {tag : [] for tag in top_tags}


for item in itemsLookup:
    for tag in rawCluster:
        if tag in itemsLookup[item]:
            rawCluster[tag].append(item)

clusters = list(rawCluster.items())

overlaps = []
for i in range(1, len(clusters)):
    for j in range(i):
        s_i = set(clusters[i][1])
        s_j = set(clusters[j][1])
        size_i = len(s_i)
        size_j = len(s_j)
        union = len(s_i | s_j)
        intersection = len(s_i & s_j)
        perc = str(round(intersection/union*100, 2)) + "%"
        overlaps.append(
                            (
                            clusters[j][0], #tag1
                            clusters[i][0], #tag2
                            size_j, #size tag1
                            size_i, #size tag2
                            perc, #percentage overlap
                            intersection, # absolute intersection
                            union # total indexed space
                            )
                        )

with open("reports/overlap.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["tag1", "tag2", "size1", "size2", "overlap%", "overlap(abs)", "union"])
    writer.writerows(overlaps)



# removing one tag
    
indexed = []
for tag in rawCluster:
    indexed += rawCluster[tag]

# items indexed by the top tags (100)
indexed = set(indexed)
count = len(indexed)
contribution = []
for tag in rawCluster:
    items = []
    for t in rawCluster:
        if t != tag:
            items += rawCluster[t]
    remaining = len(set(items))
    diff = count - remaining
    contribution += [(tag, remaining, count, str(round((diff/count)*100, 2)) + "%",  diff)]

with open("reports/contribution.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["tag_removed", "indexed", "total", "diff%", "diff(abs)"])
    writer.writerows(contribution)



