import csv
import re


__IGNORE__ = ['with', 'for', 'from', 'that', 'and', 'you', 'your', 'all', 'will', 'can', 'their',
              'are', 'into', 'this', 'through', 'more', 'take', 'has', 'one', 'have', 'out', 'features',
              'they', 'his', 'who', 'first', 'each', 'where', 'over', 'set', 'including', 'but', 'own',
              'most', 'also', 'must', 'use', 'them', 'other', 'now', 'which', 'mode', 'only', 'its', 'based',
              'while', 'back', 'like', 'than', 'two', 'before', 'when', 'even', 'ever', 'get', 'what', 'been',
              'using', 'every', 'takes', 'become', 'down', 'was', 'not', 'her', 'she', 'about', 'him', 'his',
              'then', 'after', 'goes', 'later', 'there', 'himself', 'herself', 'just', 'between', 'new',
              'make', 'way', 'both', 'once', 'well', 'find']

def removePlurals(tagList:list[str]):
    """
    Improve, problems:
    across -> acros (correct: across)
    parties -> partie (correct: party)
    """
    tagSet = set()
    for tag in tagList:
        word = tag
        notlatin = True
        es = False
        try:
            suff = tag[-2:]
            if suff in ['us', 'os']:
                notlatin = False
        except:
            ...
        
        if tag[-1] == 's' and len(tag) > 4 and notlatin:
            print(word)
            word = tag[:-1]
            print(word)
            if input() == '5': exit()
        tagSet.add(word)


def tagSplit(tags:str) -> list[str]:
    tagList = tags.split("|")                       # separate tags
    tagList = [tag.lower() for tag in tagList]      # make lower case
    # removePlurals(tagList)
    tagList = list(set(tagList) - set(__IGNORE__))  # remove ignore words
    return tagList

def getItems(entities:list[str, str]):
    items = []
    for title, tags in entities:
        cleanTags = tagSplit(tags)
        items.append((title, cleanTags))
    return items

def topTags(items:list[str, list[str]], th):
    """Extract the top [th] tags from the inventory"""
    tagCount = dict()
    for _, tags in items:
        for t in tags:
            try:
                tagCount[t] += 1
            except:
                tagCount[t] = 1
        # we don't need EVERY tag
        if len(tagCount) > th:
            break
    tagCount = list(tagCount.items())
    tagCount.sort(key=lambda a: a[1], reverse=True)
    tagCount = dict(tagCount)
    return tagCount
    
def sharedTags(catTags:dict[int,list[str]], c):
    from functools import reduce
    tags = [ set(catTags[i].keys()) for i in catTags]
    shared = reduce(lambda a, b: a & b, tags)
    cumulativeTags = {t : 0 for t in shared}
    for tag in shared:
        v = [catTags[key][tag] for key in catTags]
        cumulativeTags[tag] = min(v)
    
    return cumulativeTags



def getRecs(items:list[str, list[str]], tag:str, clusters:list[str], leaves:list[str], depth=1):
    # leaves aren't excluded, they are padding if all else fails    
    itemLookup = dict(items)
    coset = set(clusters) - {tag}
    exclusive = dict() # candidates
    for item in itemLookup:
        itemTags = itemLookup[item]
        # if the tags include the cluster but not the other clusters
        if tag in itemTags and (set(itemTags) & coset) == set():
            exclusive[item] = len(itemTags)

    recs = []
    pad = []
    for item in exclusive:
        if exclusive[item] < depth*50 and len(recs) <= 4:
            (pad if item in leaves else recs).append(item)

    if len(recs) < 4:
        recs += pad
        recs = recs[:4]

    return recs


def getClusters(path:list[str], leaves=dict()):
    __CLUSTER__ = 4
    __THRESHOLD__ = 10000
    __DEPTH__ = 4 # FOR NOW
    
    catalogues = []
    i = 0
    while(True):
        try:
            i += 1
            fp = open("drop/items" + str(i) + '.csv', "r", encoding="utf-8")
            catalogues.append((i, getItems(list(csv.reader(fp))[1:])))
        except:
            if i > 10:
                break
    
    # parse tags:
    # we want the top n tags from each catalogue and then based on the top ones
    # catTags = {index : [tags, ...], }
    catTags = {}
    for index, cat in catalogues: #remove 0 when you're done cleaning csv
        t = topTags(cat, __THRESHOLD__)
        catTags[index] = t
    
    cumulativeTags = sharedTags(catTags, __CLUSTER__)
    
    c = list(cumulativeTags.items())
    c.sort(key=lambda a: a[1])
    clusters = list(dict(c[-4:]).keys())
    print(clusters)
    "put a return here and make a function"
    
    "the variable leaves, which contains items already picked as reps will be passed to the function"
    catLookup = dict(catalogues)
    branch = { tag : { i : [] for i in catLookup } for tag in clusters}
    for tag in clusters:
        for i in catLookup:
            branch[tag][i] = getRecs(catLookup[i], tag, clusters, [])

    print(branch)

    return branch
    

def main():
    
    """
    {'tag' : {'index' : ['reps', ], ...},
    ...}
    """
    getClusters()

    """
    TODO:
    1 - update path/leaves variables
    2 - integrate path variable in getCluster function
    3 - assign ids to clusters a store somewhere
    ...
    """



    """cluster found, next:
    1 - extract from each category 4 representatives
    2 - call the function to find the sub clusters, passing the current one and the items selected
    3 - loop for n cycles
    4 - write to csv the results"""

if __name__ == '__main__':
    main()


