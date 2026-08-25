# Dictionary Methods and Concepts Practice

# Creating dictionaries
dic = {
    "name": "shahid",
    "age": 18,
    "comp": "fladdra"
}
print("Original:", dic)

# Accessing values
print("Name:", dic["name"])
print("Age (get):", dic.get("age"))
print("Missing key (get):", dic.get("missing", "default_value"))

# keys(): return view of keys
print("Keys:", dic.keys())
print("List of keys:", list(dic.keys()))

# values(): return view of values
print("Values:", dic.values())
print("List of values:", list(dic.values()))

# items(): return view of (key, value) tuples
print("Items:", dic.items())
print("List of items:", list(dic.items()))

# Iterating over keys
for key in dic.keys():
    print(f"Key: {key}")

# Iterating over values
for value in dic.values():
    print(f"Value: {value}")

# Iterating over items (key, value pairs)
for key, value in dic.items():
    print(f"{key}: {value}")

# update(): update dictionary with another dictionary
upd = {"name": "shahid", "age": 18, "comp": "fladdra"}
upd.update({"age": 19, "city": "New York"})
print("After update:", upd)

# pop(): remove specific key and return value
pop_dic = {"name": "shahid", "age": 18, "comp": "fladdra"}
removed = pop_dic.pop("age")
print("Removed age:", removed)
print("After pop:", pop_dic)

# popitem(): remove and return last inserted key-value pair
pitm = {"name": "shahid", "age": 18, "comp": "fladdra"}
last_item = pitm.popitem()
print("Popped item:", last_item)
print("After popitem:", pitm)

# clear(): remove all items
clr = {"name": "shahid", "age": 18, "comp": "fladdra"}
clr.clear()
print("After clear:", clr)

# copy(): shallow copy
cpy = {"name": "shahid", "age": 18, "comp": "fladdra"}
a = cpy.copy()
a["age"] = 19
print("Original:", cpy)
print("Copy:", a)

# get(): get value with default (already shown above)

# setdefault(): get value, set default if key missing
sd = {"name": "shahid"}
print("setdefault age:", sd.setdefault("age", 20))
print("After setdefault:", sd)

# fromkeys(): create dict from keys with same value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("From keys:", new_dict)

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(5)}
print("Squares dict:", squares_dict)

# Conditional dict comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares dict:", even_squares)

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print("Merged (|):", merged)

# Update in-place with |= (Python 3.9+)
dict1 |= dict2
print("After |=:", dict1)

# Check if key exists
print("'name' in dic:", "name" in dic)
print("'missing' in dic:", "missing" in dic)

# len(): number of key-value pairs
print("Length:", len(dic))

# max, min on keys
print("Max key:", max(dic))
print("Min key:", min(dic))

# sorted keys
print("Sorted keys:", sorted(dic.keys()))

# Nested dictionaries
nested = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print("Nested:", nested)
print("User1 name:", nested["user1"]["name"])

# Access nested safely with get
print("Safe access:", nested.get("user3", {}).get("name", "Not found"))

# Delete key
del dic["comp"]
print("After del comp:", dic)

# Dictionary view objects are dynamic
keys_view = dic.keys()
dic["new_key"] = "new_value"
print("Dynamic keys view:", list(keys_view))

# dict() constructor
from_list = dict([("a", 1), ("b", 2)])
print("From list of tuples:", from_list)

from_kwargs = dict(name="John", age=30)
print("From kwargs:", from_kwargs)