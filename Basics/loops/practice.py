# Loops Concepts Practice

# ============================================
# FOR LOOP BASICS
# ============================================

# range(start, stop, step)
for i in range(5):
    print(i, end=" ")
print()

for i in range(1, 10, 2):
    print(i, end=" ")
print()

# Reverse loop
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Loop over string
for ch in "python":
    print(ch, end=" ")
print()

# Loop over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over tuple and set
for t in (1, 2, 3):
    print(t, end=" ")
print()
for s in {10, 20, 30}:
    print(s, end=" ")
print()

# Loop over dictionary
d = {"name": "shahid", "age": 18}
for key in d:
    print(key, d[key])
for key, value in d.items():
    print(key, value)

# ============================================
# WHILE LOOP
# ============================================

count = 1
while count <= 5:
    print("while:", count)
    count += 1

# while with user-style condition (infinite loop + break)
num = 0
while True:
    num += 1
    if num >= 3:
        break

# ============================================
# BREAK AND CONTINUE
# ============================================

# break: exit loop completely
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("(break at 5)")

# continue: skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("(only odd)")

# pass: do nothing (placeholder)
for i in range(3):
    pass  # TODO later

# ============================================
# ELSE WITH LOOPS
# ============================================
# else runs only if loop completed without break

for i in range(5):
    print(i, end=" ")
else:
    print("(loop finished normally)")

for i in range(10):
    if i == 5:
        break
else:
    print("this will NOT print")

# Prime check using for-else
n = 13
for i in range(2, n):
    if n % i == 0:
        print(n, "is not prime")
        break
else:
    print(n, "is prime")

# ============================================
# NESTED LOOPS
# ============================================

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# ============================================
# ENUMERATE: index + value
# ============================================

langs = ["py", "js", "go"]
for idx, lang in enumerate(langs):
    print(idx, lang)

# custom start index
for idx, lang in enumerate(langs, start=1):
    print(idx, lang)

# ============================================
# ZIP: iterate multiple sequences together
# ============================================

names = ["a", "b", "c"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(name, score)

# zip stops at shortest list
nums1 = [1, 2, 3]
nums2 = [10, 20]
print(list(zip(nums1, nums2)))

# ============================================
# REVERSED AND SORTED ITERATION
# ============================================

for r in reversed([1, 2, 3]):
    print(r, end=" ")
print()

for s in sorted([3, 1, 2]):
    print(s, end=" ")
print()

# ============================================
# LOOP PATTERNS / TRICKS
# ============================================

# Sum of numbers
total = 0
for i in range(1, 6):
    total += i
print("Sum 1..5 =", total)

# Find max without max()
mx = None
for i in [4, 9, 2, 7]:
    if mx is None or i > mx:
        mx = i
print("Max =", mx)

# Count occurrences
cnt = 0
for ch in "banana":
    if ch == "a":
        cnt += 1
print("'a' appears", cnt, "times")

# Multiplication table
n = 3
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Fibonacci series
a, b = 0, 1
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b
print()

# Factorial
fact = 1
for i in range(1, 6):
    fact *= i
print("5! =", fact)

# Sum of digits
num = 12345
s = 0
while num > 0:
    s += num % 10
    num //= 10
print("Digit sum =", s)

# Reverse number
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed =", rev)