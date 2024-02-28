

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
    common = []
    # trashWords = ['a', 'the', 'of', 'with', 'that', 'for', 'from', 'and']
    trashWords = ['a', 'the']
    trashWords = trashWords
    for word in trashWords:
        try:
            common.append(tagCount[word])
        except:
            "the word isn't in the description"
    try:
        th = min(common)
    except:
        th = 3
    relevant = []
    for tag in tagCount:
        if tagCount[tag] < th and len(tag) in range(3,12):
            relevant.append(tag.strip())
    
    return relevant



fout = open("winetags.csv", "w", encoding='utf-8', newline="")
with open("wine.csv", "r", encoding="latin-1", newline="") as fin:
    reader = csv.reader(fin, delimiter=',')
    writer = csv.writer(fout, delimiter=',')

    reader.__next__()
    writer.writerow(['item', 'tags'])
    # wordSep = re.compile("[^a-zA-Z]")
    for title, tags in reader:
        # rawTags = wordSep.split(tags)
        rawTags = tags.split("|")
        cleanTags = tagSearch(rawTags)
        try:
            cleanTags[40]
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




