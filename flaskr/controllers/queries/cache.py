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
    cache = db["user_cache"]
    updates = db['updates']
    updateCache(cache, item, tags)
    countUpdates(updates, item)


def getCache(n_elementi):
    db = connect()
    cache = db["user_cache"]
    results = []
    for doc in cache.find(projection={"_id": 0}).sort("update", -1).limit(n_elementi):
        results.append(doc)
    print(results)
    return results


def getTopitems(n):
    db = connect()
    updates = db['updates']
    top_count_update = updates.find().sort("updates_count", -1).limit(n)
    top_items = [doc["item"] for doc in top_count_update]
    user_cache = db['user_cache']
    items_from_user = user_cache.find({"item": {"$in": top_items}})
    print(list(items_from_user))
    return list(items_from_user)

# items = [
#     {'Title':{'stranger': 5, 'drama': 8, 'boone': 3, 'florence': 2}},
#     { 'Art_name':{'abstract': 10, 'contemporary': 7, 'publisher': 5}},
#     {'Giochi':{ 'build': 5, 'invest': 2, 'demolish': 8}}
# ]

# collection.insert_many(items)
# getCache(3)
# update("Title", ["stranger", "drama", "boone", "Florence", "white"])
# getTopitems("MuseDB", "updates", "user_cache", 2)
# updateCache(collection, updates, "Title1", ["stranger1", "drama1", "white1"])
# updateCache(collection, updates,"Art_name2", ["abstract", "contemporary", "publisher3"])
# getCache(3)