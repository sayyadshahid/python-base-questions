# ============================================================
# BIG O NOTATION - Complete Concepts
# ============================================================

# What is Big O Notation?
# ------------------------
# Big O Notation is a way to describe how the runtime or space
# requirements of an algorithm grow as the input size grows.
# It helps us compare different algorithms and choose the best one.

# Think of it like this: If you have 10 items vs 1,000,000 items,
# how much longer will your program take? Big O answers that.

# ============================================================
# 1. WHY DO WE NEED BIG O?
# ============================================================

# We use Big O because:
# 1. Hardware differences - Fast computer vs slow computer
# 2. Programming language differences - Python vs C++
# 3. Focus on growth rate - How does time increase with input size?

# Example: If Algorithm A takes 2n time and Algorithm B takes n^2 time:
# n = 10:   A = 20 ops,   B = 100 ops
# n = 100:  A = 200 ops,  B = 10,000 ops
# n = 1000: A = 2000 ops, B = 1,000,000 ops
# As n grows, Algorithm A is much better!

# ============================================================
# 2. COMMON BIG O COMPLEXITIES (Best to Worst)
# ============================================================

# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)

# Visual growth rates:
# n       | O(1) | O(log n) | O(n) | O(n log n) | O(n^2)
# --------|------|----------|------|------------|-------
# 1       | 1    | 0        | 1    | 0          | 1
# 10      | 1    | 3.3      | 10   | 33         | 100
# 100     | 1    | 6.6      | 100  | 660        | 10,000
# 1000    | 1    | 10       | 1000 | 10,000     | 1,000,000

# ============================================================
# 3. O(1) - CONSTANT TIME
# ============================================================

# Execution time does NOT change with input size.
# Same time whether you have 10 items or 10 million items.

def get_first_element(arr):
    """Accessing first element - O(1)"""
    return arr[0]

def check_if_exists(hash_map, key):
    """Dictionary lookup - O(1)"""
    return key in hash_map

def push_to_stack(stack, value):
    """Stack push - O(1)"""
    stack.append(value)

# Examples of O(1) operations:
# - Accessing array element by index: arr[5]
# - Dictionary/hash map lookup: d[key]
# - Stack push/pop
# - Queue enqueue/dequeue (with deque)
# - Variable assignment

print("O(1) Examples:")
my_list = [1, 2, 3, 4, 5]
print(f"  First element: {get_first_element(my_list)}")
my_dict = {"a": 1, "b": 2}
print(f"  Key exists: {check_if_exists(my_dict, 'a')}")

# ============================================================
# 4. O(log n) - LOGARITHMIC TIME
# ============================================================

# The problem size is HALVED with each step.
# Very efficient! Even with million items, few operations needed.

def binary_search(arr, target):
    """Binary search - O(log n)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Why O(log n)?
# 1,000,000 items -> ~20 steps (2^20 ≈ 1,000,000)
# 1,000,000,000 items -> ~30 steps

print("\nO(log n) Examples:")
sorted_arr = list(range(1, 101))  # [1, 2, 3, ..., 100]
print(f"  Binary search for 50 in 1-100: index {binary_search(sorted_arr, 50)}")

# Other O(log n) examples:
# - Binary search in sorted array
# - Finding parent/child in binary heap
# - Balanced BST operations (search, insert, delete)
# - Exponentiation by squaring

# ============================================================
# 5. O(n) - LINEAR TIME
# ============================================================

# The time grows DIRECTLY with input size.
# Look at every element once.

def find_max(arr):
    """Find maximum - O(n)"""
    max_val = arr[0]
    for num in arr:  # Loops through all n elements
        if num > max_val:
            max_val = num
    return max_val

def linear_search(arr, target):
    """Linear search - O(n)"""
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def sum_all(arr):
    """Sum all elements - O(n)"""
    total = 0
    for num in arr:
        total += num
    return total

# Examples of O(n) operations:
# - Finding max/min in unsorted array
# - Linear search
# - Counting occurrences
# - Reversing a string/array
# - Copying an array

print("\nO(n) Examples:")
nums = [3, 7, 1, 9, 4, 2]
print(f"  Max in {nums}: {find_max(nums)}")
print(f"  Linear search for 9: index {linear_search(nums, 9)}")

# ============================================================
# 6. O(n log n) - LINEARITHMIC TIME
# ============================================================

# Combination of linear and logarithmic.
# Best comparison-based sorting algorithms.

def merge_sort(arr):
    """Merge sort - O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Why O(n log n)?
# - Divide array in half: log n levels
# - At each level, merge n elements: O(n)
# - Total: O(n log n)

print("\nO(n log n) Examples:")
unsorted = [38, 27, 43, 3, 9, 82, 10]
sorted_result = merge_sort(unsorted)
print(f"  Merge sort: {unsorted} -> {sorted_result}")

# Other O(n log n) examples:
# - Quick sort (average case)
# - Heap sort
# - Tim sort (Python's built-in sorted())
# - Tree sort

# ============================================================
# 7. O(n^2) - QUADRATIC TIME
# ============================================================

# Nested loops - for each element, loop through all elements.
# Problem size doubles -> Time quadruples!

def bubble_sort(arr):
    """Bubble sort - O(n^2)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_duplicates(arr):
    """Find duplicates - O(n^2)"""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Examples of O(n^2) operations:
# - Bubble sort, Selection sort, Insertion sort
# - Comparing all pairs
# - Finding duplicates (naive approach)
# - Matrix operations

print("\nO(n^2) Examples:")
arr_to_sort = [64, 34, 25, 12, 22, 11, 90]
print(f"  Bubble sort: {bubble_sort(arr_to_sort.copy())}")

# ============================================================
# 8. O(n^3) - CUBIC TIME
# ============================================================

# Triple nested loops.
# Used in some matrix multiplication algorithms.

def matrix_multiply(A, B):
    """Naive matrix multiplication - O(n^3)"""
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Examples of O(n^3) operations:
# - Naive matrix multiplication
# - Some dynamic programming problems
# - Floyd-Warshall algorithm (shortest paths)

print("\nO(n^3) Examples:")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(f"  Matrix multiply: {result}")

# ============================================================
# 9. O(2^n) - EXPONENTIAL TIME
# ============================================================

# Time doubles with each additional input element.
# Very slow! Only usable for small inputs (n < 40).

def fibonacci_recursive(n):
    """Fibonacci (naive recursive) - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def power_set(arr):
    """Generate all subsets - O(2^n)"""
    if not arr:
        return [[]]

    first = arr[0]
    rest_power_set = power_set(arr[1:])

    new_subsets = []
    for subset in rest_power_set:
        new_subsets.append([first] + subset)

    return rest_power_set + new_subsets

# Why O(2^n)?
# Each element can either be included or excluded = 2 choices
# For n elements: 2 * 2 * 2 ... = 2^n combinations

print("\nO(2^n) Examples:")
print(f"  Fibonacci(10): {fibonacci_recursive(10)}")
print(f"  Power set of [1,2,3]: {power_set([1, 2, 3])}")

# ============================================================
# 10. O(n!) - FACTORIAL TIME
# ============================================================

# Extremely slow! Grows faster than exponential.
# Only works for very small inputs (n < 12).

def permutations(arr):
    """Generate all permutations - O(n!)"""
    if len(arr) <= 1:
        return [arr]

    result = []
    for i, num in enumerate(arr):
        rest = arr[:i] + arr[i + 1:]
        for perm in permutations(rest):
            result.append([num] + perm)

    return result

# Why O(n!)?
# First choice: n options, Second: n-1, Third: n-2, ...
# Total: n * (n-1) * (n-2) * ... * 1 = n!

print("\nO(n!) Examples:")
print(f"  Permutations of [1,2,3]: {permutations([1, 2, 3])}")
print(f"  Permutations of [1,2,3,4]: {permutations([1, 2, 3, 4])}")

# ============================================================
# 11. SPACE COMPLEXITY
# ============================================================

# Big O also measures how much MEMORY an algorithm uses.

def constant_space(n):
    """O(1) space - Fixed memory regardless of input"""
    total = 0
    for i in range(n):
        total += i
    return total

def linear_space(arr):
    """O(n) space - Creates array proportional to input"""
    return [x * 2 for x in arr]

def quadratic_space(n):
    """O(n^2) space - Creates n x n structure"""
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        matrix.append(row)
    return matrix

print("\nSpace Complexity Examples:")
print(f"  O(1) space: {constant_space(10)}")
print(f"  O(n) space: {linear_space([1, 2, 3])}")
print(f"  O(n^2) space: {quadratic_space(3)}")

# ============================================================
# 12. HOW TO ANALYZE TIME COMPLEXITY
# ============================================================

# Rules:
# 1. Drop constants: O(2n) -> O(n)
# 2. Drop lower terms: O(n^2 + n) -> O(n^2)
# 3. Loops: for i in range(n) -> O(n)
# 4. Nested loops: O(n) * O(n) = O(n^2)
# 5. Sequential statements: Add complexities
# 6. If-else: Take the WORST case

def analyze_example(n):
    # O(n) loop
    for i in range(n):
        print(i)

    # O(n^2) nested loop
    for i in range(n):
        for j in range(n):
            print(i, j)

# Total: O(n) + O(n^2) = O(n^2) (drop lower term)

# ============================================================
# 13. BEST, AVERAGE, AND WORST CASE
# ============================================================

# Best Case: Minimum time (best input)
# Average Case: Expected time (average input)
# Worst Case: Maximum time (worst input)

def linear_search_v2(arr, target):
    """
    Best case: O(1) - target is first element
    Average case: O(n/2) = O(n) - target is in middle
    Worst case: O(n) - target is last or not present
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

print("\nBest/Average/Worst Case:")
test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  Best case (search 1): index {linear_search_v2(test_arr, 1)}")
print(f"  Worst case (search 10): index {linear_search_v2(test_arr, 10)}")

# ============================================================
# 14. AMORTIZED ANALYSIS
# ============================================================

# Amortized = Average time over a sequence of operations.
# Some operations may be slow, but most are fast.

# Example: Python list append
# - Usually O(1) - just add to end
# - Occasionally O(n) - when list needs to resize
# - Amortized O(1) - average over many appends

def amortized_example():
    lst = []
    for i in range(100):
        lst.append(i)  # Usually O(1), occasionally O(n) for resize
    return lst

print("\nAmortized Analysis:")
print(f"  List of 100 elements created (amortized O(1) per append)")

# ============================================================
# 15. QUICK REFERENCE TABLE
# ============================================================

"""
| Big O        | Name          | Example                    | When to Use           |
|-------------|---------------|----------------------------|-----------------------|
| O(1)        | Constant      | Array index access         | Always fast           |
| O(log n)    | Logarithmic   | Binary search              | Searching sorted data |
| O(n)        | Linear        | Single loop                | Simple processing     |
| O(n log n)  | Linearithmic  | Merge sort                 | Efficient sorting     |
| O(n^2)      | Quadratic     | Nested loops               | Simple sorting        |
| O(n^3)      | Cubic         | Matrix multiply            | Small matrices        |
| O(2^n)      | Exponential   | Fibonacci recursive        | Small n only          |
| O(n!)       | Factorial     | Permutations               | Very small n only     |
"""

# ============================================================
# 16. PRACTICAL EXAMPLES
# ============================================================

# Problem 1: What's the complexity?
def mystery_function(n):
    count = 0
    i = 1
    while i < n:
        j = 0
        while j < n:
            count += 1
            j += 2
        i *= 2
    return count

# Answer: O(n log n)
# Outer loop: log n (i doubles each time)
# Inner loop: n/2 (j increases by 2)
# Total: n * log n

print("\nPractical Examples:")
print(f"  mystery_function(16) = {mystery_function(16)}")

# Problem 2: Compare two algorithms
def algorithm_a(n):
    """O(n)"""
    return sum(range(n))

def algorithm_b(n):
    """O(n^2)"""
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total

n = 1000
import time

start = time.time()
algorithm_a(n)
time_a = time.time() - start

start = time.time()
algorithm_b(n)
time_b = time.time() - start

print(f"\n  Algorithm A (O(n)): {time_a:.6f}s")
print(f"  Algorithm B (O(n^2)): {time_b:.6f}s")
print(f"  Algorithm A is {time_b/time_a:.1f}x faster!")
