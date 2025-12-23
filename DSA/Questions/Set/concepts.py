# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set1:", set1, "→ Used as first set for operations")
print("Set2:", set2, "→ Used as second set for operations")
print('=================================================================')
# Adding elements
set1.add(8)
print("After add():", set1, "→ add() is used to insert ONE element into a set")
print('=================================================================')

set1.update([9, 10])
print("After update():", set1, "→ update() is used to insert MULTIPLE elements")
print('=================================================================')

# Removing elements
set1.remove(10)
print("After remove():", set1, "→ remove() deletes element and gives error if not found")
print('=================================================================')

set1.discard(100)
print("After discard():", set1, "→ discard() deletes element WITHOUT error if not found")
print('=================================================================')

removed = set1.pop()
print("After pop():", set1, "→ pop() removes a RANDOM element")
print("Popped element:", removed, "→ This element was randomly removed")
print('=================================================================')

# Copying set
set3 = set1.copy()
print("Copied Set:", set3, "→ copy() creates a duplicate of the set")
print('=================================================================')

# Set operations
print("Union:", set1.union(set2),
      "→ union() combines both sets and removes duplicates")
print('=================================================================')

print("Intersection:", set1.intersection(set2),
      "→ intersection() returns common elements")
print('=================================================================')

print("Difference:", set1.difference(set2),
      "→ difference() returns elements present in set1 but not in set2")
print('=================================================================')

print("Symmetric Difference:", set1.symmetric_difference(set2),
      "→ symmetric_difference() returns uncommon elements")
print('=================================================================')

# Update operations
set1.update(set2)
print("After update():", set1,
      "→ update() adds all elements of set2 into set1")
print('=================================================================')

set1 = {1, 2, 3, 4, 5}
set1.intersection_update(set2)
print("After intersection_update():", set1,
      "→ intersection_update() keeps only common elements")
print('=================================================================')

set1 = {1, 2, 3, 4, 5}
set1.difference_update(set2)
print("After difference_update():", set1,
      "→ difference_update() removes elements of set2 from set1")
print('=================================================================')

set1 = {1, 2, 3, 4, 5}
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update():", set1,
      "→ keeps only elements not common in both sets")
print('=================================================================')

# Relationship checking
print("Is subset:", {1, 2}.issubset(set2),
      "→ issubset() checks whether one set is inside another")
print('=================================================================')

print("Is superset:", set2.issuperset({4, 5}),
      "→ issuperset() checks whether a set contains another set")
print('=================================================================')

print("Is disjoint:", set1.isdisjoint({100, 200}),
      "→ isdisjoint() checks if no common elements exist")
print('=================================================================')

# Built-in functions
print("Length:", len(set2),
      "→ len() returns number of elements")

print("Max:", max(set2),
      "→ max() returns highest value")

print("Min:", min(set2),
      "→ min() returns smallest value")

print("Sum:", sum(set2),
      "→ sum() returns total of elements")

print("Sorted:", sorted(set2),
      "→ sorted() returns elements in sorted LIST form")
print('=================================================================')

# Membership
print("4 in set2:", 4 in set2,
      "→ checks whether element exists in set")
print('=================================================================')

print("10 not in set2:", 10 not in set2,
      "→ checks whether element does not exist")

print('=================================================================')
# Clearing set
set2.clear()
print("After clear():", set2,
      "→ clear() removes all elements and makes set empty")
