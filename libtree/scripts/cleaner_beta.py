

import csv
import re

__IGNORE__ = ['with', 'for', 'from', 'that', 'and', 'you', 'your', 'all', 'will', 'can', 'their',
              'are', 'into', 'this', 'through', 'more', 'take', 'has', 'one', 'have', 'out', 'features',
              'they', 'his', 'who', 'first', 'each', 'where', 'over', 'set', 'including', 'but', 'own',
              'most', 'also', 'must', 'use', 'them', 'other', 'now', 'which', 'mode', 'only', 'its', 'based',
              'while', 'back', 'like', 'than', 'two', 'before', 'when', 'even', 'ever', 'get', 'what', 'been',
              'using', 'every', 'takes', 'become', 'down']


def tagSearch(tags:list[str]) -> list[str]:
    tags = [t.lower() for t in tags]
    unique = set(tags)
    tagCount = {t : 0 for t in unique}
    for tag in tags:
        tagCount[tag] += 1

    relevant = []
    for tag in tagCount:
        if len(tag) in range(3,12):
            relevant.append(tag.strip())
    
    return relevant


fout = open("itemtags.csv", "w", encoding='utf-8', newline="")
with open("item.csv", "r", encoding="utf-8", newline="") as fin:
    reader = csv.reader(fin, delimiter=',')
    writer = csv.writer(fout, delimiter=',')

    reader.__next__()
    writer.writerow(['item', 'tags'])
    wordSep = re.compile("[^a-zA-Z'-]")
    for title, tags in reader:
        rawTags = wordSep.split(tags)
        cleanTags = tagSearch(rawTags)
        try:
            cleanTags[10]
            cleanTags = list(set(cleanTags) - set(__IGNORE__))
            # print(cleanTags[:10])
            tagText = '|'.join(cleanTags)
            writer.writerow([title, tagText])
        except:
            "less than 10 tags"
        # bye = input()
        # if bye == '0':
        #     break
fout.close()




