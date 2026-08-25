# Pattern Programs Practice

# ============================================
# RIGHT TRIANGLE (star) - increasing
# ============================================
# *
# * *
# * * *
n = 5
for i in range(1, n + 1):
    print("* " * i)

print()

# ============================================
# INVERTED RIGHT TRIANGLE - decreasing
# ============================================
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(n, 0, -1):
    print("* " * i)

print()

# ============================================
# LEFT ALIGNED MIRROR (right aligned pyramid)
# ============================================
#     *
#   * *
# * * *
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print()

# ============================================
# PYRAMID (centered)
# ============================================
#     *
#    * *
#   * * *
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)

print()

# ============================================
# INVERTED PYRAMID
# ============================================
# * * * * *
#  * * * *
#   * * *
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

print()

# ============================================
# DIAMOND
# ============================================
#   *
#  * *
# * * *
#  * *
#   *
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

print()

# ============================================
# HOLLOW SQUARE
# ============================================
# * * * * *
# *       *
# *       *
# * * * * *
rows = cols = 5
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ============================================
# NUMBER TRIANGLE (same number in row)
# ============================================
# 1
# 2 2
# 3 3 3
for i in range(1, n + 1):
    print((str(i) + " ") * i)

print()

# ============================================
# CONSECUTIVE NUMBERS TRIANGLE
# ============================================
# 1
# 2 3
# 4 5 6
num = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(num, end=" ")
        num += 1
    print()

print()

# ============================================
# REVERSE NUMBER TRIANGLE
# ============================================
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

# ============================================
# PALINDROMIC NUMBER PYRAMID
# ============================================
#     1
#   1 2 1
# 1 2 3 2 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print()

# ============================================
# BINARY TRIANGLE
# ============================================
# 1
# 0 1
# 1 0 1
# 0 1 0 1
for i in range(1, n + 1):
    start = 1 if i % 2 != 0 else 0
    val = start
    for _ in range(i):
        print(val, end=" ")
        val = 1 - val      # toggle between 0 and 1
    print()

print()

# ============================================
# FLOYD'S TRIANGLE
# ============================================
num = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(num, end=" ")
        num += 1
    print()

print()

# ============================================
# ALPHABET TRIANGLE (increasing)
# ============================================
# A
# A B
# A B C
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

print()

# ============================================
# SAME LETTER TRIANGLE
# ============================================
# A
# B B
# C C C
for i in range(n):
    print((chr(65 + i) + " ") * (i + 1))

print()

# ============================================
# SQUARE GRID OF NUMBERS
# ============================================
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for i in range(rows):
    for j in range(1, cols + 1):
        print(j, end=" ")
    print()

print()

# ============================================
# BUTTERFLY PATTERN
# ============================================
# *        *
# **      **
# ***    ***
# ********
# ********
# ***    ***
# **      **
# *        *
half = 4
for i in range(1, half + 1):
    print("*" * i + " " * (2 * (half - i)) + "*" * i)
for i in range(half, 0, -1):
    print("*" * i + " " * (2 * (half - i)) + "*" * i)

print()

# ============================================
# HOURGLASS PATTERN
# ============================================
for i in range(half, 0, -1):
    print(" " * (half - i) + "* " * i)
for i in range(1, half + 1):
    print(" " * (half - i) + "* " * i)

print()

# ============================================
# PLUS / CROSS PATTERN
# ============================================
size = 5
mid = size // 2
for i in range(size):
    if i == mid:
        print("* " * size)
    else:
        row = [" "] * size
        row[mid] = "*"
        print(" ".join(row))