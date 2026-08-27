# ============================================================
# STRINGS - Complete Concepts
# ============================================================

# What is a String?
# -----------------
# A string is a sequence of characters enclosed in quotes.
# Strings are IMMUTABLE in Python - once created, cannot be changed.

# ============================================================
# 1. CREATING STRINGS
# ============================================================

# Single quotes
s1 = 'Hello'
# Double quotes
s2 = "World"
# Triple quotes (multiline)
s3 = """This is
a multiline
string"""
# Escape characters
s4 = "He said, \"Hello\""
s5 = "Line1\nLine2"  # \n = newline
s6 = "Tab\there"      # \t = tab
s7 = "Backslash \\"   # \\ = backslash

print("Creating Strings:")
print(f"  Single quotes: {s1}")
print(f"  Double quotes: {s2}")
print(f"  Triple quotes:\n{s3}")
print(f"  Escape chars: {s4}")

# ============================================================
# 2. STRING INDEXING AND SLICING
# ============================================================

text = "Python Programming"
# Index:    0 1 2 3 4 5 6 7 ...
# Reverse: -18-17-16-15-14...

print("\nIndexing:")
print(f"  First char: {text[0]}")    # P
print(f"  Last char: {text[-1]}")    # g
print(f"  6th char: {text[5]}")      # o

print("\nSlicing:")
print(f"  [0:6]: {text[0:6]}")       # Python
print(f"  [:6]: {text[:6]}")         # Python (same as above)
print(f"  [7:]: {text[7:]}")         # Programming
print(f"  [-11:]: {text[-11:]}")     # Programming
print(f"  [::2]: {text[::2]}")       # Pto rgamn (every 2nd char)
print(f"  [::-1]: {text[::-1]}")     # gnimmargorP nohtyP (reverse)

# ============================================================
# 3. STRING METHODS - CASE CONVERSION
# ============================================================

word = "  Hello World  "

print("\nCase Methods:")
print(f"  Original: '{word}'")
print(f"  upper(): '{word.upper()}'")      # HELLO WORLD
print(f"  lower(): '{word.lower()}'")      # hello world
print(f"  title(): '{word.title()}'")      # Hello World
print(f"  capitalize(): '{word.capitalize()}'")  # Hello world
print(f"  swapcase(): '{'Hello'.swapcase()}'")   # hELLO
print(f"  casefold(): '{'Straße'.casefold()}'")  # strasse (aggressive lower)

# ============================================================
# 4. STRING METHODS - STRIPPING/TRIMMING
# ============================================================

padded = "  Hello World  "

print("\nStrip Methods:")
print(f"  Original: '{padded}'")
print(f"  strip(): '{padded.strip()}'")       # Hello World
print(f"  lstrip(): '{padded.lstrip()}'")     # Hello World  (remove left)
print(f"  rstrip(): '{padded.rstrip()}'")     #   Hello World (remove right)
print(f"  strip('Hd'): '{'Hello World'.strip('Hd')}'")  # ello Worl

# ============================================================
# 5. STRING METHODS - SEARCHING
# ============================================================

sentence = "Python is awesome, Python is fun"

print("\nSearch Methods:")
print(f"  find('Python'): {sentence.find('Python')}")        # 0 (first occurrence)
print(f"  rfind('Python'): {sentence.rfind('Python')}")      # 23 (last occurrence)
print(f"  index('Python'): {sentence.index('Python')}")      # 0 (same as find)
print(f"  count('Python'): {sentence.count('Python')}")      # 2
print(f"  startswith('Python'): {sentence.startswith('Python')}")  # True
print(f"  endswith('fun'): {sentence.endswith('fun')}")      # True
print(f"  'awesome' in sentence: {'awesome' in sentence}")   # True

# find vs index: find returns -1 if not found, index raises ValueError
print(f"  find('Java'): {sentence.find('Java')}")  # -1
# print(sentence.index('Java'))  # Would raise ValueError

# ============================================================
# 6. STRING METHODS - REPLACING AND SPLITTING
# ============================================================

text2 = "Hello World Python World"

print("\nReplace Methods:")
print(f"  replace('World', 'There'): '{text2.replace('World', 'There')}'")
print(f"  replace('World', 'There', 1): '{text2.replace('World', 'There', 1)}'")  # Replace first only

print("\nSplit Methods:")
print(f"  split(): {text2.split()}")                    # ['Hello', 'World', 'Python', 'World']
print(f"  split(' '): {text2.split(' ')}")              # Same as above
print(f"  split('o'): {text2.split('o')}")              # ['Hell', ' W', 'rld Pyth', 'n W', 'rld']
print(f"  rsplit(' ', 1): {text2.rsplit(' ', 1)}")     # Split from right, max 1 split
print(f"  partition('Python'): {text2.partition('Python')}")  # ('Hello World ', 'Python', ' World')
print(f"  splitlines(): {'Line1\nLine2\nLine3'.splitlines()}")  # ['Line1', 'Line2', 'Line3']

# ============================================================
# 7. STRING METHODS - JOINING
# ============================================================

words = ["Python", "is", "awesome"]

print("\nJoin Methods:")
print(f"  ' '.join(words): {' '.join(words)}")           # Python is awesome
print(f"  '-'.join(words): {'-'.join(words)}")           # Python-is-awesome
print(f"  ''.join(words): {''.join(words)}")             # Pythonisawesome
print(f"  ', '.join(['a', 'b', 'c']): {', '.join(['a', 'b', 'c'])}")  # a, b, c

# ============================================================
# 8. STRING METHODS - CHECKING CONTENT
# ============================================================

print("\nCheck Methods:")
print(f"  'hello'.isalpha(): {'hello'.isalpha()}")       # True (all letters)
print(f"  '123'.isdigit(): {'123'.isdigit()}")           # True (all digits)
print(f"  'abc123'.isalnum(): {'abc123'.isalnum()}")     # True (letters + digits)
print(f"  '   '.isspace(): {'   '.isspace()}")           # True (all whitespace)
print(f"  'Hello World'.istitle(): {'Hello World'.istitle()}")  # True (Title Case)
print(f"  'HELLO'.isupper(): {'HELLO'.isupper()}")       # True (all uppercase)
print(f"  'hello'.islower(): {'hello'.islower()}")       # True (all lowercase)
print(f"  '12345'.isnumeric(): {'12345'.isnumeric()}")   # True (all numeric)
print(f"  '12.34'.isdecimal(): {'12.34'.isdecimal()}")   # False (has dot)
print(f"  'abc'.isidentifier(): {'abc'.isidentifier()}") # True (valid variable name)
print(f"  '  '.isprintable(): {'  '.isprintable()}")     # True

# ============================================================
# 9. STRING FORMATTING
# ============================================================

name = "Alice"
age = 25
pi = 3.14159

print("\nString Formatting:")

# f-strings (Python 3.6+) - RECOMMENDED
print(f"  f-string: {name} is {age} years old")
print(f"  f-string with expression: {name} will be {age + 5} in 5 years")
print(f"  f-string with format: Pi = {pi:.2f}")  # 3.14
print(f"  f-string padding: '{name:>10}'")       # '     Alice'
print(f"  f-string left align: '{name:<10}'")    # 'Alice     '
print(f"  f-string center: '{name:^10}'")        # '  Alice   '
print(f"  f-string with fill: '{name:*^10}'")    # '**Alice***'

# format() method
print("  format(): {} is {} years old".format(name, age))
print("  format numbered: {1} is {0}".format("first", "second"))

# % formatting (old style)
print("  %% formatting: %s is %d years old" % (name, age))

# ============================================================
# 10. STRING CONCATENATION
# ============================================================

print("\nConcatenation:")
a = "Hello"
b = "World"
print(f"  Using +: {a + ' ' + b}")
print(f"  Using join: {' '.join([a, b])}")

# String repetition
print(f"  Repeat '*': {'*' * 20}")
print(f"  Repeat '-': {'-=' * 10}")

# ============================================================
# 11. STRING IMMUTABILITY
# ============================================================

print("\nImmutability:")
s = "Hello"
# s[0] = 'h'  # TypeError: 'str' object does not support item assignment
# To modify, create a new string:
s = 'h' + s[1:]
print(f"  Modified string: {s}")  # hello

# Or use join
s = ''.join(['H', 'e', 'l', 'l', 'o'])
print(f"  Using join: {s}")

# ============================================================
# 12. STRING ITERATION
# ============================================================

print("\nIteration:")
word = "Python"

# Character by character
for char in word:
    print(f"  {char}", end=" ")
print()

# With index using enumerate
for i, char in enumerate(word):
    print(f"  {i}:{char}", end=" ")
print()

# ============================================================
# 13. STRING ENCODING
# ============================================================

print("\nEncoding:")
text3 = "Hello"
encoded = text3.encode('utf-8')
print(f"  Original: {text3}")
print(f"  Encoded: {encoded}")
print(f"  Decoded: {encoded.decode('utf-8')}")

# ord() and chr()
print(f"  ord('A'): {ord('A')}")   # 65
print(f"  chr(65): {chr(65)}")     # A
print(f"  ord('a'): {ord('a')}")   # 97

# ============================================================
# 14. STRING COMPARISON
# ============================================================

print("\nComparison:")
print(f"  'apple' == 'apple': {'apple' == 'apple'}")    # True
print(f"  'apple' < 'banana': {'apple' < 'banana'}")    # True (lexicographic)
print(f"  'abc' < 'abd': {'abc' < 'abd'}")              # True
print(f"  'ABC' < 'abc': {'ABC' < 'abc'}")              # True (uppercase < lowercase)

# ============================================================
# 15. COMMON STRING PATTERNS
# ============================================================

print("\nCommon Patterns:")

# Reverse a string
reversed_str = "hello"[::-1]
print(f"  Reverse 'hello': {reversed_str}")

# Check palindrome
def is_palindrome(s):
    return s == s[::-1]
print(f"  Is 'racecar' palindrome: {is_palindrome('racecar')}")
print(f"  Is 'hello' palindrome: {is_palindrome('hello')}")

# Count vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
print(f"  Vowels in 'Hello World': {count_vowels('Hello World')}")

# Remove duplicates (preserve order)
def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))
print(f"  Remove duplicates 'abracadabra': {remove_duplicates('abracadabra')}")

# ============================================================
# 16. USEFUL STRING OPERATIONS
# ============================================================

print("\nUseful Operations:")

# Check if string is empty
s_empty = ""
print(f"  Is empty (not s): {not s_empty}")  # True

# Get character frequency
from collections import Counter
freq = Counter("hello")
print(f"  Frequency of 'hello': {dict(freq)}")

# Convert list to string
char_list = ['P', 'y', 't', 'h', 'o', 'n']
result = ''.join(char_list)
print(f"  List to string: {result}")

# String to list
string = "Hello"
char_list = list(string)
print(f"  String to list: {char_list}")

# Find all substrings
def all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

print(f"  Substrings of 'abc': {all_substrings('abc')}")

# ============================================================
# 17. STRING CONSTANTS
# ============================================================

import string

print("\nString Constants:")
print(f"  ASCII letters: {string.ascii_letters}")    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"  ASCII lowercase: {string.ascii_lowercase}")  # abcdefghijklmnopqrstuvwxyz
print(f"  ASCII uppercase: {string.ascii_uppercase}")  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"  Digits: {string.digits}")                    # 0123456789
print(f"  Punctuation: {string.punctuation}")          # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(f"  Whitespace: {repr(string.whitespace)}")      # ' \t\n\r\x0b\x0c'

# ============================================================
# 18. PRACTICAL EXAMPLES
# ============================================================

print("\nPractical Examples:")

# 1. Title case a sentence
def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())
print(f"  Title case 'hello world': '{to_title_case('hello world')}'")

# 2. Check if string is anagram
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(f"  Is 'listen' and 'silent' anagram: {is_anagram('listen', 'silent')}")

# 3. Caesar cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
print(f"  Caesar cipher 'Hello' shift 3: {caesar_cipher('Hello', 3)}")
print(f"  Caesar cipher decode 'Khoor' shift 3: {caesar_cipher('Khoor', -3)}")

# 4. Word count
def word_count(s):
    return len(s.split())
print(f"  Word count 'Hello World': {word_count('Hello World')}")

# 5. Longest word
def longest_word(s):
    return max(s.split(), key=len)
print(f"  Longest word 'I love Python programming': {longest_word('I love Python programming')}")
