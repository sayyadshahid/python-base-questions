# {keys: values}
dic = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}

print(dic)


# access all keys
print(dic.keys())

for dic in dic.keys():
    print(dic)

# print values


dict = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}
print(dict.values())

for dict in dict.values():
    print(dict)

# items --> return new obj as a touples


itm = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}

print(itm.items())

for key, value in itm.items():
    print(key, value)
    

# update ----> update the dictionary with anothe rdictionary
upd = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}


upd.update({"age": 19})
print(upd)


# pop ----> remove specific data and return 

pop = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}


bb = pop.pop("age")

print(pop)
print(bb)

# popitem()------> remove and return last inserted key

pitm = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}

aa = pitm.popitem()

print(pitm)
print(aa)


# clear ------> remove all items from dictionay 
# clr = {
#     "name": "shahid",
#     "age": 18,
#     "comp": "fladdra"
# }


# clr.clear()
# print(clr)

# # copy
# cpy = {
#     "name": "shahid",
#     "age": 18,
#     "comp": "fladdra"
# }


# a = cpy.copy()
# a["age"] = 19
# print(cpy)
# print(a)