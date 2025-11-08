# FIFO (First In, First Out) — the first element added is the first one removed.
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)

print(queue[0])
# .

a = []
a.append(20)
a.append(20)
a.append(20)
a.append(20)

print(a)
