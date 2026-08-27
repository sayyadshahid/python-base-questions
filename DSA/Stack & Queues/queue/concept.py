# ============================================================
# QUEUE - Complete Concepts
# ============================================================

# What is a Queue?
# ----------------
# A Queue is a linear data structure that follows the FIFO
# (First In, First Out) principle.
# The first element added is the first one to be removed.
# Think of it like a queue at a ticket counter - first come, first served.

# Real-life examples:
# - Printer job scheduling
# - CPU task scheduling
# - BFS (Breadth-First Search) traversal
# - Customer service systems
# - Message queues in distributed systems

# ============================================================
# 1. QUEUE OPERATIONS
# ============================================================

# enqueue()  - Add element to the rear (end) of the queue
# dequeue()  - Remove element from the front (beginning) of the queue
# peek()     - Return the front element without removing it
# isEmpty()  - Check if the queue is empty
# isFull()   - Check if the queue is full (for fixed-size arrays)
# size()     - Return the number of elements in the queue

# ============================================================
# 2. QUEUE IMPLEMENTATION USING DEQUE (Python)
# ============================================================

from collections import deque

queue = deque()

# Enqueue operation
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueues:", queue)  # deque([10, 20, 30])

# Dequeue operation
dequeued = queue.popleft()
print("Dequeued:", dequeued)  # 10
print("Queue after dequeue:", queue)  # deque([20, 30])

# Peek operation
front = queue[0]
print("Front element:", front)  # 20

# isEmpty check
print("Is empty?", len(queue) == 0)  # False

# Size
print("Size:", len(queue))  # 2

# ============================================================
# 3. QUEUE IMPLEMENTATION USING LIST (Basic)
# ============================================================

# Using list is inefficient because popleft() is O(n)
queue_list = []
queue_list.append(1)  # enqueue
queue_list.append(2)
queue_list.append(3)
print("\nList Queue:", queue_list)

# Inefficient dequeue (shifts all elements)
dequeued = queue_list.pop(0)
print("Dequeued:", dequeued)
print("After dequeue:", queue_list)

# Better to use deque for O(1) operations on both ends

# ============================================================
# 4. QUEUE IMPLEMENTATION USING LINKED LIST
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow - Cannot dequeue from empty queue")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        print(f"Dequeued: {temp.data}")
        return temp.data

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):
        return self._size

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue (front -> rear):", " -> ".join(elements))

# Example usage
q = QueueLinkedList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # Queue (front -> rear): 10 -> 20 -> 30
q.peek()     # Front element: 10
q.dequeue()  # Dequeued: 10
q.display()  # Queue (front -> rear): 20 -> 30

# ============================================================
# 5. QUEUE OVERFLOW AND UNDERFLOW
# ============================================================

# Queue Overflow: When trying to enqueue into a full queue
# (Occurs in fixed-size array implementation)

# Queue Underflow: When trying to dequeue from an empty queue
# Always check isEmpty() before dequeuing!

# ============================================================
# 6. TYPES OF QUEUES
# ============================================================

# 6.1 Circular Queue
# ------------------
# In a circular queue, the last position connects back to the first.
# This reuses empty spaces created by dequeue operations.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full (Overflow)")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty (Underflow)")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {value}")
        return value

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        i = self.front
        elements = []
        while True:
            elements.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Circular Queue:", " -> ".join(elements))

print("\n--- Circular Queue ---")
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.enqueue(40)
cq.display()

# 6.2 Double Ended Queue (Deque)
# ------------------------------
# Deque allows insertion and deletion from both ends.
# Can function as both stack and queue.

deque_queue = deque()
deque_queue.append(1)       # Add to rear
deque_queue.append(2)
deque_queue.appendleft(0)   # Add to front
print("\nDeque:", deque_queue)  # deque([0, 1, 2])

deque_queue.pop()           # Remove from rear
deque_queue.popleft()       # Remove from front
print("After operations:", deque_queue)  # deque([1])

# 6.3 Priority Queue
# -------------------
# Elements are dequeued based on priority, not order of insertion.
# Lower value = higher priority (by default in Python's heapq)

import heapq

priority_queue = []
heapq.heappush(priority_queue, 3)
heapq.heappush(priority_queue, 1)
heapq.heappush(priority_queue, 2)
print("\nPriority Queue:", priority_queue)  # Min-heap structure

print("Dequeued (highest priority):", heapq.heappop(priority_queue))  # 1
print("Dequeued:", heapq.heappop(priority_queue))  # 2

# ============================================================
# 7. TIME COMPLEXITY
# ============================================================

# Deque implementation (recommended):
# enqueue()  - O(1)
# dequeue()  - O(1)
# peek()     - O(1)
# isEmpty()  - O(1)
# size()     - O(1)

# Linked List implementation:
# enqueue()  - O(1)
# dequeue()  - O(1)
# peek()     - O(1)
# isEmpty()  - O(1)
# size()     - O(1)

# List implementation (NOT recommended):
# enqueue()  - O(1)
# dequeue()  - O(n)  <-- SLOW! shifts all elements
# peek()     - O(1)

# ============================================================
# 8. QUEUE APPLICATIONS
# ============================================================

# 1. BFS (Breadth-First Search) - Graph/Tree traversal
# 2. CPU Scheduling - Round-robin algorithm
# 3. Disk Scheduling - FCFS (First Come First Serve)
# 4. Printer Spooling - Print jobs processed in order
# 5.缓冲区 - Buffers for streaming data (IO buffers)
# 6. Message Queues - RabbitMQ, Kafka, etc.
# 7. Sliding Window - Maximum in sliding window of size k
# 8. Async Task Processing - Celery, Background jobs

# ============================================================
# 9. COMMON PROBLEMS
# ============================================================

# Problem 1: Implement queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, value):
        self.stack1.append(value)
        print(f"Enqueued: {value}")

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is Empty")
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

print("\n--- Queue Using Two Stacks ---")
qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
print("Dequeued:", qs.dequeue())  # 1
print("Dequeued:", qs.dequeue())  # 2

# Problem 2: Generate numbers with digits 5 and 6
def generate_numbers(n):
    from collections import deque
    q = deque()
    q.append("5")
    q.append("6")
    result = []
    for i in range(n):
        num = q.popleft()
        result.append(num)
        q.append(num + "5")
        q.append(num + "6")
    return result

print("\nFirst 10 numbers with digits 5 and 6:")
print(generate_numbers(10))
# ['5', '6', '55', '56', '65', '66', '555', '556', '565', '566']

# Problem 3: Sliding Window Maximum
def sliding_window_max(arr, k):
    from collections import deque
    dq = deque()
    result = []

    for i in range(len(arr)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

print("\nSliding Window Maximum:")
print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]

# Problem 4: First Non-Repeating Character in Stream
def first_non_repeating(stream):
    from collections import deque, Counter
    q = deque()
    count = Counter()
    result = []

    for char in stream:
        count[char] += 1
        q.append(char)
        while q and count[q[0]] > 1:
            q.popleft()
        result.append(q[0] if q else '#')

    return ''.join(result)

print("\nFirst non-repeating character stream:")
print(first_non_repeating("aabc"))  # a#aa
