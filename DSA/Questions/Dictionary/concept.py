# Creating dictionaries
dict1 = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

dict2 = {
    3: "Mango",
    4: "Orange",
    5: "Grapes"
}

print("Dictionary1:", dict1, "→ Used as first dictionary")
print("Dictionary2:", dict2, "→ Used as second dictionary")
print('=================================================================')

# Accessing value using key
print("Value of key 2:", dict1[2],
      "→ Keys are used to access values")
print('=================================================================')

# Using get()
print("Value using get():", dict1.get(3),
      "→ get() returns value without error if key not found")
print('=================================================================')

# Adding new key-value pair
dict1[4] = "Pineapple"
print("After adding element:", dict1,
      "→ New key-value pair added using assignment")
print('=================================================================')

# Updating existing value
dict1[2] = "Papaya"
print("After update:", dict1,
      "→ Existing value updated using key")
print('=================================================================')

# Using update() method
dict1.update({5: "Guava"})
print("After update():", dict1,
      "→ update() is used to add multiple key-value pairs")
print('=================================================================')

# Removing elements using pop()
removed = dict1.pop(3)
print("After pop():", dict1,
      "→ pop() removes element using key")
print("Removed value:", removed,
      "→ This value was removed from dictionary")
print('=================================================================')

# Removing last inserted item
last = dict1.popitem()
print("After popitem():", dict1,
      "→ popitem() removes last inserted key-value pair")
print("Removed item:", last)
print('=================================================================')

# Copying dictionary
dict3 = dict1.copy()
print("Copied Dictionary:", dict3,
      "→ copy() creates a duplicate dictionary")
print('=================================================================')

# Keys, Values, Items
print("Keys:", dict1.keys(),
      "→ keys() returns all keys")
print('=================================================================')

print("Values:", dict1.values(),
      "→ values() returns all values")
print('=================================================================')

print("Items:", dict1.items(),
      "→ items() returns key-value pairs as tuples")
print('=================================================================')

# Checking membership
print("Is key 1 present:", 1 in dict1,
      "→ checks if key exists in dictionary")
print('=================================================================')

# Length of dictionary
print("Length:", len(dict1),
      "→ len() returns number of key-value pairs")
print('=================================================================')

# Clearing dictionary
dict1.clear()
print("After clear():", dict1,
      "→ clear() removes all key-value pairs")
