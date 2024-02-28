





import csv
with open("tags.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()
    tags = [(tag, int(count)) for tag, count in reader]

with open("videogame_tags.csv", "r", encoding="utf-8", newline="") as fp:
    reader =csv.reader(fp)
    reader.__next__()
    games = dict([(item, tag.split("|")) for item, tag in reader])


k = 10

c_tags = list(dict(tags[:k]).keys())
rawCluster = {tag : [] for tag in c_tags}

for game in games:
    for tag in rawCluster:
        if tag in games[game]:
            rawCluster[tag].append(game)


with open("clusters.md", "w", encoding="utf-8") as fp:
    for tag in rawCluster:
        print(tag)
        print(rawCluster[tag][0:10])
        fp.write("\n# " + tag + ":\n")
        fp.write(',\n'.join(rawCluster[tag]))
    

print("wrote files")

rawCopy = rawCluster
# overlaps
for tag in rawCluster:
    rawCluster[tag] = set(rawCluster[tag])

clusters = list(rawCluster.items())
overlaps = []

# clusters -> [ (0 tag, 1 [items, ...]), ...]
for i in range(1, len(clusters)):
    for j in range(i):
        s_j = clusters[j][1]
        s_i = clusters[i][1]
        size_j = len(s_j)
        size_i = len(s_i)
        union = len(s_i | s_j)
        intersection = len(s_i & s_j)
        overlaps.append({clusters[j][0] : {'size' : size_j},
                         clusters[i][0] : {'size' : size_i},
                         'overlap' : {
                             'normal' : (round(intersection/union, 3)),
                             'absolute' : intersection},
                             'total' : union})

fp = open("log.md", "w") 
fp.write("\n# Pairwise overlap\n\nHow much overlap is there between clusters, studied pairwise\n\n")
for item in overlaps:
    fp.write(str(item) + '\n')
    print(item)

indexed = []
# what happens if you remove a tag from the cluster
for tag in rawCopy:
    indexed += rawCopy[tag]

indexed = set(indexed)
count = len(indexed)

removeCluster = {tag : 0 for tag in rawCluster}
for tag in rawCluster:
    items = set()
    for t in rawCluster:
        if t != tag:
            items |= rawCluster[t]
    removeCluster[tag] = len(items)

fp.write('\n\n# Removing tags \n\nWhat happens if I remove a tag?\n\n')
for tag in removeCluster:
    c = removeCluster[tag]
    out = f"Removing {tag}, yields {c} of {count} items\nA difference of {(100*(count - c)/count):0.2f}% ({count - c} absolute)"
    fp.write(out + '\n')
    print(out)

















