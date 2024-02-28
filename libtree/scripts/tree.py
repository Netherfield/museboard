import csv

with open("tags.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    reader.__next__()
    tags = [(tag, int(count)) for tag, count in reader]

with open("videogame_tags.csv", "r", encoding="utf-8", newline="") as fp:
    reader =csv.reader(fp)
    reader.__next__()
    games = dict([(item, tag.split("|")) for item, tag in reader])


clusters = []
cluster_size = 4
c_tags = list(dict(tags[:cluster_size]).keys())
coset = {tag : (set(c_tags) - {tag}) for tag in c_tags}
rawCluster = {tag : [] for tag in c_tags}
reps = rawCluster
tag_lookup = dict(tags)
# for game in games:
#     for tag in rawCluster:
#         game_tags = games[game]
#         if tag in game_tags:
#             if (coset[tag] & set(game_tags) == set()):
#                 reps[tag] += [game]
#             rawCluster[tag].append(game)

top = { tag : [] for tag in rawCluster}
for tag in rawCluster:
    for game in games:
        game_tags = games[game]
        if tag in game_tags:
            if (coset[tag] & set(game_tags) == set()):
                reps[tag] += [game]
                # len dependent on depth, the deeper, the more tags we need to find matches
                if len(game_tags) < 20 and len(top[tag]) < 10:
                    few_tags = game_tags
                    print(tag, game)
                    for t in few_tags:
                        
                        try:
                            # some tags have been removed
                            print(t, tag_lookup[t])
                        except: ...
                    top[tag].append(game)

print(top)

# if len(reps[tag]) < 10:
#     print(tag, reps[tag])

