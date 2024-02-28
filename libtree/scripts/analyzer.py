

import csv



def readChunk(reader, size):

    next = True
    while(next):
        chunk = []
        i = 0
        while (i < size):
            try:
                line = reader.__next__()
                chunk.append(line)
            except:
                next = False
                break
            i += 1
        yield chunk
    return None

vgLines = sum(1 for _ in open("videogame_tags.csv"))

with open("videogame_tags.csv", "r", encoding="utf-8", newline="") as fin:
    reader = csv.reader(fin, delimiter=',')
    reader.__next__()

    topTag = (None, 0)
    cycle = 0
    allTags = dict()
    for chunk in readChunk(reader, 100):
        cycle += 1
        print(f"Read {cycle*100} lines out of {vgLines}")
        rTags = []
        for line in chunk:
            rTags += line[1].split("|")
        
        index = set(rTags)
        countTags = { t : 0 for t in index}
        for tag in rTags:
            countTags[tag] += 1

        for key in countTags:
            c = countTags[key]
            try:
                allTags[key] += c
                up = allTags[key]
                if up > topTag[1]:
                    topTag = (key, up)
            except:
                allTags[key] = c
                if c > topTag[1]:
                    topTag = (key, c)

        print(f"Total different tags {len(allTags)}, the top tag being '{topTag[0]}' with {topTag[1]} occurrences")

    
with open("tagdump.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(['tag', 'count'])
    for key in allTags:
        writer.writerow([key, allTags[key]])


# fp = open("ignore.txt", "w", encoding="utf-8")
# fp.close()