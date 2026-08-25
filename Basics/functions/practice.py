# Functions Concepts Practice

# ============================================
# BASIC FUNCTIONS
# ============================================

def hello():
    print("hello function")

hello()

# function with parameters and return
def add(a, b):
    return a + b

print(add(2, 6))

# ============================================
# DEFAULT PARAMETERS
# ============================================

def greet(name="guest", msg="welcome"):
    print(f"hi {name}, {msg}")

greet()
greet("shahid")
greet("shahid", "good morning")
# keyword arguments (order doesn't matter)
greet(msg="bye", name="furqan")

# mutable default argument pitfall
def add_item(item, items=[]):   # shared list! avoid
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))   # [1, 2] - same list reused

# correct way
def add_item_safe(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_safe(1))
print(add_item_safe(2))   # [2]

# ============================================
# *args: variable number of positional args
# ============================================

def total(*args):
    print("args:", args)
    return sum(args)

print(total(1, 2, 3, 4))

# ============================================
# **kwargs: variable number of keyword args
# ============================================

def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

profile(name="shahid", age=18, city="mumbai")

# combining all types
def full(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

full(1, 3, 5, 7, x=10)

# unpacking with * and **
nums = [1, 2]
print(add(*nums))          # unpack list into arguments

info = {"a": 10, "b": 20}
print(add(**info))         # unpack dict into arguments

# ============================================
# RETURN MULTIPLE VALUES
# ============================================

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1, 7])
print(low, high)

# ============================================
# DOCSTRINGS
# ============================================

def square(n):
    """Return n multiplied by itself."""
    return n * n

print(square(4))
print(square.__doc__)

# ============================================
# LAMBDA (anonymous functions)
# ============================================

square_l = lambda x: x ** 2
print(square_l(5))

add_l = lambda a, b: a + b
print(add_l(3, 4))

# lambda with sorted key
students = [("shahid", 80), ("ali", 95), ("john", 70)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks)

# lambda with map / filter / reduce
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
print(squares, evens, product)

# ============================================
# MAP, FILTER, ZIP built-ins
# ============================================

names = ["alice", "bob"]
upper = list(map(str.upper, names))
print(upper)

lengths = {n: len(n) for n in map(lambda x: x, names)}
print(lengths)

# ============================================
# RECURSION
# ============================================

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(8)])

# sum of digits recursively
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))

# ============================================
# NESTED FUNCTIONS AND CLOSURES
# ============================================

def outer(msg):
    def inner():
        print("inner says:", msg)
    inner()

outer("hello")

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))

# ============================================
# GLOBAL / LOCAL / NONLOCAL
# ============================================

counter = 0            # global

def increase():
    global counter     # modify global variable
    counter += 1

increase()
increase()
print(counter)

def outer_nonlocal():
    count = 0
    def inc():
        nonlocal count # modify enclosing scope variable
        count += 1
        return count
    inc()
    inc()
    return count

print(outer_nonlocal())

# ============================================
# FUNCTION AS FIRST-CLASS OBJECT
# ============================================

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    print(func("Hello World"))

speak(shout)
speak(whisper)

# ============================================
# DECORATORS
# ============================================

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_decorator
def greet_all():
    print("hello everyone")

greet_all()

# decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("hi!")

say_hi()

# ============================================
# GENERATOR FUNCTIONS (yield)
# ============================================

def countdown(n):
    while n > 0:
        yield n          # pause and return value
        n -= 1

for num in countdown(3):
    print(num)

gen = countdown(2)
print(next(gen), next(gen))

def even_gen(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

print(list(even_gen(10)))

# generator expression
sq_gen = (x*x for x in range(5))
print(list(sq_gen))

# ============================================
# TYPE HINTS
# ============================================

def typed_add(a: int, b: int) -> int:
    return a + b

print(typed_add(2, 3))

def typed_greet(name: str) -> str:
    return f"hi {name}"

print(typed_greet("shahid"))

# ============================================
# BUILT-IN USEFUL FUNCTIONS
# ============================================

# all / any
print(all([True, True]), any([False, True]))

# callable check
print(callable(hello))

# getattr-style: function attributes
hello.description = "just prints hello"
print(hello.description)