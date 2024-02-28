
import csv
import re

# ig_list = []
__IGNORE__ = ['with', 'for', 'from', 'that', 'and', 'you', 'your', 'all', 'will', 'can', 'their',
              'are', 'into', 'this', 'through', 'more', 'take', 'has', 'one', 'have', 'out', 'features',
              'they', 'his', 'who', 'first', 'each', 'where', 'over', 'set', 'including', 'but', 'own',
              'most', 'also', 'must', 'use', 'them', 'other', 'now', 'which', 'mode', 'only', 'its', 'based',
              'while', 'back', 'like', 'than', 'two', 'before', 'when', 'even', 'ever', 'get', 'what', 'been',
              'using', 'every', 'takes', 'become', 'down', 'was', 'not', 'her', 'she', 'about', 'him', 'his',
              'then', 'after', 'goes', 'later', 'there', 'himself', 'herself', 'just', 'between', 'new',
              'make', 'way', 'both', 'once', 'well', 'find']


fileTranslator = {
    1 : "videogame",
    2 : "book",
    3 : "wine",
    4 : "car"
 }

items = []
i = 0
while(True):
    try:
        i += 1
        fp = open("drop/items" + str(i) + '.csv', "r", encoding="utf-8", newline="")
        items += list(map(lambda a: (a[0], a[1] + "|" + fileTranslator[i]) ,list(csv.reader(fp))[1:]))
        fp.close()
    except:
        if i > 10:
            break
splitter = re.compile("[^a-zA-Z']")
clean = []
for item, tags in items:
    rTags = splitter.split(tags)
    parse = []
    for tag in rTags:
        t = tag.strip()
        if len(t) > 2 and t not in __IGNORE__:
            parse.append(t)
    if len(parse) > 0:
        parse = '|'.join(parse)
        clean += [(item, parse)]


with open("reports/items.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(['item', 'tags'])
    writer.writerows(clean)

