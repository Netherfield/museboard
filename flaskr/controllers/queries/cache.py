import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["MuseDB"]
collection = db["user_cache"]
updates = db['updates']

def updateCache(collection, tr_results, item, tags):
    query = {"item": item}
    result = collection.update_one(query, {"$inc": {f"tags.{tag}": 1 for tag in tags}}, upsert=True)
    if result.upserted_id:
        print(f"Elemento '{item}' con tags '{tags}' non trovato. Nuovo elemento creato.")
    else:
        print(f"Elemento '{item}' con tags '{tags}' Trovato e aggiornato")
    tracked_query = {"item": item}
    tr_results = updates.update_one(tracked_query,{"$inc":{f"update_count": 1}}, upsert=True)



def getCache(n_elementi):
    results = []
    for doc in collection.find(projection={"_id": 0}).sort("update", -1).limit(n_elementi):
        results.append(doc)
    print(results)
    return results


def getTopitems(n):
    updates = db['updates']
    top_count_update = updates.find().sort("updates_count", -1).limit(n)
    top_items = [doc["item"] for doc in top_count_update]
    user_cache = db['user_cache']
    items_from_user = user_cache.find({"item": {"$in": top_items}})
    print(list(items_from_user))
    return list(items_from_user)

items = [
    {'Title':{'stranger': 5, 'drama': 8, 'boone': 3, 'florence': 2}},
    { 'Art_name':{'abstract': 10, 'contemporary': 7, 'publisher': 5}},
    {'Giochi':{ 'build': 5, 'invest': 2, 'demolish': 8}}
]

# collection.insert_many(items)
# getCache(3)
# updateCache(collection, updates, "Title", ["stranger", "drama", "boone", "Florence", "white"])
# getTopitems("MuseDB", "updates", "user_cache", 2)
# updateCache(collection, updates, "Title1", ["stranger1", "drama1", "white1"])
# updateCache(collection, updates,"Art_name2", ["abstract", "contemporary", "publisher3"])
# getCache(3)