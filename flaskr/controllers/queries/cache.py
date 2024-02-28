import pymongo

def connect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["MuseDB"]
    return db

def requestStatus(log):
    def statusWrapper(func):
        def status(*args):
            if log:
                result, msg = func(*args)
                params = []
                for arg in args:
                    s = str(arg)
                    try:
                        p = s[:10]
                        if len(s) > 10: p += '...'
                    except: p = s
                    params += [p]
                if result: print("Query with parameters", str(params), "was successful")
                else: print("Query with parameters", str(params), "was unsuccessful:\n", msg)
        return status
    return statusWrapper

@requestStatus(log=True)
def updateCache(cache, item, tags):
    query = {"item": item}
    result = cache.update_one(query, {"$inc": {f"tags.{tag}": 1 for tag in tags}}, upsert=True)
    return result.upserted_id, "Created new entry"

@requestStatus(log=True)
def countUpdates(updates, item):
    updateTracker = {"item": item}
    result = updates.update_one(updateTracker,{"$inc":{f"update_count": 1}}, upsert=True)
    return result.upserted_id, "Created new entry"

def update(item, tags):
    db = connect()
    cache = db["items_cache"]
    updates = db['updates_log']
    updateCache(cache, item, tags)
    countUpdates(updates, item)


def getTopitems(updates, n) -> list[str]:
    top_count = updates.find().sort("updates_count", -1).limit(n)
    return [entity["item"] for entity in top_count]

def getCache(cache, items:list[str]) -> list[dict]:
    itemsCache = cache.find({"item": {"$in": items}})
    return list(itemsCache)

def uncache(empty_n) -> list[dict]:
    db = connect()
    cache = db["items_cache"]
    updates = db["updates_log"]
    items = getTopitems(updates, empty_n)
    return getCache(cache, items) 


# items = {
#         'Title':{'stranger': 5, 'drama': 8, 'boone': 3, 'florence': 2},
#         'Art_name':{'abstract': 10, 'contemporary': 7, 'publisher': 5},
#         'Giochi':{ 'build': 5, 'invest': 2, 'demolish': 8}
#         }

# for item in items:
#     update(item, list(items[item].keys()))

# collection.insert_many(items)
# getCache(3)
# update("Title", ["stranger", "drama", "boone", "Florence", "white"])
# getTopitems("MuseDB", "updates", "user_cache", 2)
# updateCache(collection, updates, "Title1", ["stranger1", "drama1", "white1"])
# updateCache(collection, updates,"Art_name2", ["abstract", "contemporary", "publisher3"])
# getCache(3)