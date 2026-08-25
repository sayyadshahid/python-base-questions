# Python Fundamentals Practice

# ============================================
# VARIABLES AND DATA TYPES
# ============================================

# int, float, str, bool
age = 18
height = 5.9
name = "shahid"
is_student = True
nothing = None

print(type(age), type(height), type(name), type(is_student), type(nothing))

# multiple assignment
a, b, c = 1, 2.5, "three"
x = y = z = 0

# ============================================
# TYPE CONVERSION (casting)
# ============================================

num_str = "100"
num = int(num_str)           # str -> int
flt = float(num_str)         # str -> float
back = str(100)              # int -> str
print(num + 1, flt + 0.5, back + "!")

# round, abs
pi_val = 3.14159
print(round(pi_val, 2))      # round to 2 decimals
print(abs(-10))

# int() truncates, // floor division
print(int(3.99), 7 // 2)

# ============================================
# OPERATORS
# ============================================

# arithmetic: + - * / // % **
print(7 + 2, 7 - 2, 7 * 2, 7 / 2, 7 // 2, 7 % 2, 7 ** 2)

# comparison: == != > < >= <=
print(5 == 5, 5 != 3, 4 > 2, 1 < 0)

# logical: and or not
print(True and False, True or False, not True)

# assignment shortcuts: += -= *= /= //= %= **=
n = 10
n += 5; n -= 3; n *= 2; n //= 4
print(n)

# identity: is / is not (same object in memory)
p = [1, 2]
q = [1, 2]
r = p
print(p is r, p is q, p == q)   # == compares values, is compares identity

# membership: in / not in
print("py" in "python", 3 in [1, 2, 3], "z" not in "abc")

# ============================================
# INPUT / OUTPUT
# ============================================

# f-strings (formatted string literals)
user = "shahid"
score = 95.6789
print(f"{user} scored {score:.2f}%")     # format decimals
print(f"{10:5d}|")                       # width padding
print(f"{0.25:.0%}")                     # percentage

# sep and end parameters
print("a", "b", "c", sep="-")
print("no newline", end=" | ")
print("done")

# ============================================
# STRINGS - methods and operations
# ============================================

s = "Hello World"

# case conversion
print(s.upper(), s.lower(), s.title(), s.capitalize(), s.swapcase())

# searching
print(s.find("World"), s.count("l"), "World" in s)

# strip whitespace
messy = "   hi   "
print(messy.strip(), messy.lstrip(), messy.rstrip())

# replace and split/join
print(s.replace("World", "Python"))
csv_line = "a,b,c,d"
parts = csv_line.split(",")          # split into list
joined = "-".join(parts)             # join list into string
print(parts, joined)

# check content
print("abc123".isdigit(), "abc".isalpha(), "ab12".isalnum(), "  ".isspace())

# startswith / endswith
print(s.startswith("He"), s.endswith("ld"))

# center / ljust / rjust / zfill
print("|" + s.center(20) + "|")
print("42".zfill(5), "7".rjust(3, "0"))

# ord and chr (character <-> ASCII)
print(ord("A"), chr(66))

# string immutability note:
# s[0] = "J"  -> TypeError! strings can't be changed, use replace instead
new_s = "J" + s[1:]
print(new_s)

# escape characters: \n newline \t tab \" quote \\ backslash
print("line1\nline2\ttabbed")

# raw strings keep backslashes (useful for windows paths)
print(r"C:\new\folder")

# multiline strings with triple quotes
multi = """first line
second line"""
print(multi)

# ============================================
# CONDITIONALS
# ============================================

mark = 85
if mark >= 90:
    grade = "A+"
elif mark >= 80:
    grade = "A"
elif mark >= 70:
    grade = "B"
else:
    grade = "C"
print(grade)

# ternary (conditional expression)
result = "pass" if mark >= 40 else "fail"
print(result)

# truthy / falsy values: 0, "", [], {}, None are False
if []:
    print("never prints")
if "hi":
    print("non-empty string is truthy")

# match-case (Python 3.10+)
command = "start"
match command:
    case "start":
        print("starting...")
    case "stop":
        print("stopping...")
    case _:
        print("unknown command")

# ============================================
# MATH MODULE BASICS
# ============================================

import math
print(math.sqrt(16), math.floor(3.7), math.ceil(3.2))
print(math.pi, math.pow(2, 5), math.gcd(12, 18))

# random module basics
import random
print(random.randint(1, 6))            # random int inclusive
print(random.choice(["r", "p", "s"]))  # random pick
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

# ============================================
# COMMON NUMBER CHECKS
# ============================================

val = 15
print("even" if val % 2 == 0 else "odd")
print("positive" if val > 0 else "negative")

# swap two numbers without temp variable
m, k = 5, 9
m, k = k, m
print(m, k)

# max/min of numbers
print(max(3, 7, 1), min(3, 7, 1))