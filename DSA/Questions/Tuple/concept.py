# Creating tuples
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7)

print("Tuple1:", t1, "→ Used as first tuple for operations")
print("Tuple2:", t2, "→ Used as second tuple for operations")
print('=================================================================')

# Accessing element using index
print("Element at index 2:", t1[2],
      "→ Indexing is used to access a specific element")
print('=================================================================')

# Counting elements
print("Count of 4:", t1.count(4),
      "→ count() returns how many times an element appears")
print('=================================================================')

# Finding index of element
print("Index of 3:", t1.index(3),
      "→ index() returns the position of the element")
print('=================================================================')

# Length of tuple
print("Length:", len(t1),
      "→ len() returns total number of elements in tuple")
print('=================================================================')

# Max, Min, Sum
print("Maximum:", max(t1),
      "→ max() returns the largest value")
print('=================================================================')

print("Minimum:", min(t1),
      "→ min() returns the smallest value")
print('=================================================================')

print("Sum:", sum(t1),
      "→ sum() returns total of all elements")
print('=================================================================')

# Concatenation
t3 = t1 + t2
print("Concatenated Tuple:", t3,
      "→ + operator is used to join two tuples")
print('=================================================================')

# Repetition
t4 = t1 * 2
print("Repeated Tuple:", t4,
      "→ * operator repeats tuple elements")
print('=================================================================')

# Membership checking
print("3 in t1:", 3 in t1,
      "→ checks whether element exists in tuple")
print('=================================================================')

print("10 not in t1:", 10 not in t1,
      "→ checks whether element does not exist in tuple")
print('=================================================================')

# Slicing
print("Slice t1[1:4]:", t1[1:4],
      "→ slicing extracts a part of the tuple")
print('=================================================================')

# Sorting tuple (convert to list then back to tuple)
sorted_tuple = tuple(sorted(t1))
print("Sorted Tuple:", sorted_tuple,
      "→ tuples are immutable, so sorting returns a new tuple")
print('=================================================================')

# Nested tuple
nested = ((1, 2), (3, 4))
print("Nested Tuple:", nested,
      "→ tuple inside another tuple")
print('=================================================================')

# Deleting tuple
temp = (10, 20)
print("Temporary Tuple:", temp,
      "→ created to demonstrate deletion")
print('=================================================================')

del temp
print("Tuple deleted → del removes the entire tuple")
