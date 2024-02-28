
import csv



tagList = []
with open("tagdump.csv", "r", encoding="utf-8", newline="") as fp:
    reader = csv.reader(fp)
    next(reader)


    for line in reader:
        tagList += [line]

tagList.sort(key=lambda a: int(a[1]), reverse=True)

with open("tags.csv", "w", encoding="utf-8", newline="") as fp:

    writer = csv.writer(fp)
    writer.writerow(['item', 'tag'])
    buffer = []
    discard = []
    for i, tag in enumerate(tagList):
        print(f"{tag[0]} appears {tag[1]} times\n")
        sel = input("keep? or 0 to discard, 1 to dump rest, 5 to quit")
        if sel == '5': break
        if sel == '1':
            buffer = tagList[i:]
            break
        if sel == '0':
            discard += [tag[0]]
        else:
            writer.writerow(tag)
    if buffer:
        writer.writerows(buffer)
        
print(discard)
with open("ignore.txt", "w", encoding="utf-8") as fp:
    for tag in discard:
        fp.write(tag)




