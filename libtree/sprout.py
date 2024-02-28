import csv
import re

__WEAK__ = True
__DEPTH__ = 5 # FOR NOW
__CLUSTER__ = 4
__THRESHOLD__ = 15000
__HOME__ = 'all_tags'
ig_list = ['with', 'for', 'from', 'that', 'and', 'you', 'your', 'all', 'will', 'can', 'their',
              'are', 'into', 'this', 'through', 'more', 'take', 'has', 'one', 'have', 'out', 'features',
              'they', 'his', 'who', 'first', 'each', 'where', 'over', 'set', 'including', 'but', 'own',
              'most', 'also', 'must', 'use', 'them', 'other', 'now', 'which', 'mode', 'only', 'its', 'based',
              'while', 'back', 'like', 'than', 'two', 'before', 'when', 'even', 'ever', 'get', 'what', 'been',
              'using', 'every', 'takes', 'become', 'down', 'was', 'not', 'her', 'she', 'about', 'him', 'his',
              'then', 'after', 'goes', 'later', 'there', 'himself', 'herself', 'just', 'between', 'new',
              'make', 'way', 'both', 'once', 'well', 'find']
# ig_list = []
__IGNORE__ = ig_list

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
    items = dict(items)
    return items

def topTags(items:dict[str, list[str]], th:int):
    """Extract the top [th] tags from the inventory"""
    tagCount = dict()
    for tags in items.values():
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
    
def sharedTags(catTags:dict[int,list[str]]):
    from functools import reduce
    tags = [ set(catTags[i].keys()) for i in catTags]
    shared = reduce(lambda a, b: a & b, tags)
    # if len(shared) == 0:
    #     return None
    cumulativeTags = {t : 0 for t in shared}
    for tag in shared:
        v = [catTags[key][tag] for key in catTags]
        cumulativeTags[tag] = min(v)
    
    return cumulativeTags


"unused"
def sepTags(catTags:dict[int,list[str]]):
    sepClusters = dict()
    for i in catTags:
        sepClusters[i] = list(catTags[i].keys())[:4]
        print(sepClusters)
        exit()


def getReps(items:dict[str, list[str]], tag:str, clusters:list[str], leaves:list[str], depth):
    # leaves aren't excluded, they are padding if all else fails    
    coset = set(clusters) - {tag}
    exclusive = dict() # candidates
    rest = dict()
    for item in items:
        itemTags = items[item]
        # if the tags include the cluster but not the other clusters
        if tag in itemTags:
            if (set(itemTags) & coset) == set():
                exclusive[item] = len(itemTags)
            else:
                rest[item] = len(itemTags)

    reps = []
    pad = []
    for item in exclusive:
        if exclusive[item] < (depth+1)*50 and len(reps) <= 4:
            (pad if item in leaves else reps).append(item)

    # if len(reps) < 4:
    #     reps += pad[:4]
    if len(reps) < 4:
        rest = list(rest.items())
        rest.sort(key=lambda a: a[1], reverse=True)
        rest = list(dict(rest[:4]).keys())
        reps += rest
    if reps == []:
        reps = list(exclusive.keys()) + rest + pad + leaves
    reps = reps[:4]
    return reps

def updateCat(catalogues:dict[int,dict[str,list[str]]], indices:list[int], tag:str):
    "Keep only the items in catalogues that have the tag"
    updated = { index : dict() for index in catalogues}
    for index in catalogues:
        cat = catalogues[index]
        i = 0
        for item in cat:
            if tag in cat[item] or (len(cat[item]) > 20 and i < 500 ):
                newTags = list(set(cat[item]))
                if tag in cat[item]: newTags.remove(tag) # we remove the tag here
                updated[index][item] = newTags
                i += 1
        # if len(updated[index]) < 10:
        #     print('probleeeem')

    return updated


def getClusters(catalogues:dict[int, dict[str, list[str]]], leaves:dict[int,list[str]], path:tuple[str], depth:int):
    # parse tags:
    # we want the top n tags from each catalogue and then based on the top ones
    # catTags = {index : [tags, ...], }
    catTags = {}
    for index in catalogues: #remove 0 when you're done cleaning csv
        catTags[index] = topTags(catalogues[index], __THRESHOLD__)

    "SHARE TAGS FORCES US TO WORK ONLY ON TAGS SHARED BY ALL INDEXES"
    cumulativeTags = sharedTags(catTags)

    # if cumulativeTags is not None:
    c = list(cumulativeTags.items())
    c.sort(key=lambda a: a[1])
    try:
        clusters = list(dict(c[-__CLUSTER__:]).keys())
    except:
        clusters = list(dict(c).keys())
    
    branch = { tag : { i : [] for i in catalogues } for tag in clusters}
    
    "i of existing catalogues"
    
    for tag in clusters:
        for i in branch[tag]:
            reps = getReps(catalogues[i], tag, clusters, leaves[i], depth)
            branch[tag][i] = reps

    if depth > 0:
        yield branch, path, depth
        for tag in branch:
            "index based on branches"
            catalogues = updateCat(catalogues, 'indices', tag)
            "it was giving error because I was redefining branch by unpacking it as for branch, ... in func(branch) OMFG"
            for b, p, d in getClusters(catalogues, branch[tag], path + (tag,), depth-1):
                yield b, p, d
    else:
        yield branch, path, depth

def main():
    leaves = dict()
    catalogues = []
    i = 0
    while(True):
        try:
            i += 1
            fp = open("drop/items" + str(i) + '.csv', "r", encoding="utf-8")
            catalogues.append((i, getItems(list(csv.reader(fp))[1:])))
            leaves[i] = []
        except:
            if i > 10:
                break
    catalogues = dict(catalogues)
    

    pathStart = (__HOME__,)
    branchId = { __HOME__ : 1}
    lookup = {1 : __HOME__}
    i = 2

    fp = open("tree.csv", "w", encoding="utf-8", newline="")
    writer = csv.writer(fp)
    """these will be branch, sub branch, tag, category and item
    but I will be unsufferable for a second"""
    writer.writerow(['branch', 'twig', 'bark', 'genus', 'leaf'])
    for branch, path, depth in getClusters(catalogues, leaves, pathStart, __DEPTH__):

        lineBranch = []
        
        for tag in branch:
            pathStr = ','.join(path)
            originNode = branchId[pathStr]
            p = pathStr + ',' + tag
            branchId[p] = i
            currentNode = branchId[p]
            lookup[currentNode] = tag
            for cat in branch[tag]:
                for item in branch[tag][cat]:
                    d = __DEPTH__ - depth
                    lineBranch.append([originNode, currentNode, tag, cat, item, d, p])
            i += 1
        "writebranch to csv"
        writer.writerows(lineBranch)
    fp.close()
        

if __name__ == '__main__':
    main()

    """
    TODO:
    1 - create non-indexed and indexed csvs
    2 - collect click and path data to update db
    3 - scrape for pics from google img
    """
