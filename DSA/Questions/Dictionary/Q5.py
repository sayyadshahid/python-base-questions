# 5. Create a dictionary of student grades and find the average grade.
dictt = {
    'shahid': 12,
    'safwaan': 29,
    'arham': 21,
    'arham': 60
}

total = sum(dictt.values())
avg = total / len(dictt)

print(avg)