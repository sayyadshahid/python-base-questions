# List Methods and Concepts Practice

# Creating lists
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2]]
empty_list = []

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slicing [1:4]:", my_list[1:4])
print("Slicing [::2]:", my_list[::2])
print("Reverse:", my_list[::-1])

# append: add item at the end
my_list.append("hey")
print("After append:", my_list)

# insert: insert at specific index
my_list.insert(1, "he")
print("After insert:", my_list)

# extend: merge two lists
a = [1, 2]
b = [3, 4]
a.extend(b)
print("After extend:", a)

# remove: remove first occurrence of value
rem = [1, 2, 3, 4, 2]
rem.remove(2)
print("After remove(2):", rem)

# pop: remove and return item at index (default last)
pop_list = [1, 2, 3, 4, 5, 6]
p = pop_list.pop(1)
print("Popped:", p, "Remaining:", pop_list)
last = pop_list.pop()
print("Popped last:", last, "Remaining:", pop_list)

# index: return first index of value
index_list = [1, 2, 3, 42, 2]
i = index_list.index(2)
print("Index of 2:", i)

# count: how many times value appears
count_list = [1, 2, 3, 4, 5, 6, 1, 1]
print("Count of 1:", count_list.count(1))

# sort: sort in ascending order (in-place)
sort_list = [1, 2, 4, 2, 1, 7, 65, 4]
sort_list.sort()
print("Sorted ascending:", sort_list)

# sort reverse: sort in descending order
sort_list.sort(reverse=True)
print("Sorted descending:", sort_list)

# sorted(): return new sorted list (non-mutating)
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print("Original:", original, "Sorted:", new_sorted)

# reverse: reverse list in-place
rev = [1, 2, 43, 5, 6, 7]
rev.reverse()
print("Reversed:", rev)

# copy: shallow copy
a1 = [1, 2, 43, 2, 1]
b1 = a1.copy()
b1.append(99)
print("Original:", a1, "Copy:", b1)

# clear: remove all elements
clear_list = [1, 2, 43, 5]
clear_list.clear()
print("After clear:", clear_list)

# len: length of list
x = [1, 2, 3, 4, 5]
print("Length:", len(x))

# in operator: check membership
print("3 in x:", 3 in x)
print("10 in x:", 10 in x)

# List comprehensions
squares = [x**2 for x in range(10)]
print("Squares:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)


# Nested lists (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("Element [1][2]:", matrix[1][2])

# Flatten nested list
flat = [item for row in matrix for item in row]
print("Flattened:", flat)

# min, max, sum
nums = [10, 20, 5, 40, 15]
print("Min:", min(nums), "Max:", max(nums), "Sum:", sum(nums))

# enumerate: get index and value
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")

# zip: combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# List methods that return new lists (non-mutating)
# + operator: concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print("Concatenated:", combined)

# * operator: repetition
repeated = [1, 2] * 3
print("Repeated:", repeated)

# any(), all()
print("Any true:", any([False, False, True]))
print("All true:", all([True, True, True]))