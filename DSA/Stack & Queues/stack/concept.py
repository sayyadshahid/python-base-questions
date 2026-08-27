# ============================================================
# STACK - Complete Concepts
# ============================================================

# What is a Stack?
# ----------------
# A Stack is a linear data structure that follows the LIFO
# (Last In, First Out) principle.
# The last element added is the first one to be removed.
# Think of it like a stack of plates - you add and remove from the top.

# Real-life examples:
# - Browser back button (navigation history)
# - Undo/Redo functionality in editors
# - Function call stack (recursion)
# - Expression evaluation (infix to postfix)
# - Backtracking algorithms

# ============================================================
# 1. STACK OPERATIONS
# ============================================================

# push()    - Add element to the top of the stack
# pop()     - Remove element from the top of the stack
# peek()    - Return the top element without removing it
# isEmpty() - Check if the stack is empty
# isFull()  - Check if the stack is full (only for fixed-size arrays)
# size()    - Return the number of elements in the stack

# ============================================================
# 2. STACK IMPLEMENTATION USING LIST (Python)
# ============================================================

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)  # [10, 20, 30]

# Pop operation
popped = stack.pop()
print("Popped:", popped)  # 30
print("Stack after pop:", stack)  # [10, 20]

# Peek operation
top = stack[-1]
print("Top element:", top)  # 20

# isEmpty check
print("Is empty?", len(stack) == 0)  # False

# Size
print("Size:", len(stack))  # 2

# ============================================================
# 3. STACK IMPLEMENTATION USING LINKED LIST
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed: {value}")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow - Cannot pop from empty stack")
            return None
        temp = self.top
        self.top = self.top.next
        self._size -= 1
        print(f"Popped: {temp.data}")
        return temp.data

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def size(self):
        return self._size

    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (top -> bottom):", " -> ".join(elements))

# Example usage
s = StackLinkedList()
s.push(10)
s.push(20)
s.push(30)
s.display()  # Stack (top -> bottom): 30 -> 20 -> 10
s.peek()     # Top element: 30
s.pop()      # Popped: 30
s.display()  # Stack (top -> bottom): 20 -> 10

# ============================================================
# 4. STACK OVERFLOW AND UNDERFLOW
# ============================================================

# Stack Overflow: When trying to push onto a full stack
# (Occurs in fixed-size array implementation)

# Stack Underflow: When trying to pop from an empty stack
# Always check isEmpty() before popping!

# ============================================================
# 5. TIME COMPLEXITY
# ============================================================

# All operations are O(1) in both list and linked list implementation:
# push()   - O(1)
# pop()    - O(1)
# peek()   - O(1)
# isEmpty() - O(1)
# size()   - O(1) for linked list, O(1) for list

# ============================================================
# 6. STACK APPLICATIONS
# ============================================================

# 1. Expression Evaluation - Evaluate postfix/prefix expressions
# 2. Syntax Parsing - Check balanced parentheses/brackets
#    Example: { [ ( ) ] } is balanced, { [ ( ) } is not
# 3. Backtracking - Maze solving, DFS traversal
# 4. Function Calls - Recursion uses call stack
# 5. Undo/Redo - Text editors use two stacks
# 6. Browser History - Back/Forward navigation
# 7. Tower of Hanoi - Classic recursion problem
# 8. Infix to Postfix Conversion - Shunting yard algorithm

# ============================================================
# 7. COMMON PROBLEMS
# ============================================================

# Problem 1: Check balanced parentheses
def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

print("\nBalanced check:")
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False

# Problem 2: Reverse a string using stack
def reverse_string(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print("\nReversed string:", reverse_string("Hello"))  # olleH

# Problem 3: Sort a stack (using recursion)
def sorted_insert(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    temp = stack.pop()
    sorted_insert(stack, element)
    stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)

test_stack = [30, -5, 18, 14, -3]
sort_stack(test_stack)
print("Sorted stack:", test_stack)  # [-5, -3, 14, 18, 30]

# ============================================================
# 8. TWO STACKS IN ONE ARRAY
# ============================================================

class TwoStacks:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
            return
        self.top1 += 1
        self.arr[self.top1] = value

    def push2(self, value):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
            return
        self.top2 -= 1
        self.arr[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            print("Stack Underflow")
            return None
        value = self.arr[self.top1]
        self.top1 -= 1
        return value

    def pop2(self):
        if self.top2 == self.size:
            print("Stack Underflow")
            return None
        value = self.arr[self.top2]
        self.top2 += 1
        return value

print("\nTwo Stacks in One Array:")
ts = TwoStacks(10)
ts.push1(1)
ts.push1(2)
ts.push2(10)
ts.push2(20)
print("Pop1:", ts.pop1())  # 2
print("Pop2:", ts.pop2())  # 20
