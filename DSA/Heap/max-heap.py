import heapq

arr = [10, 20, 15, 30, 40, -4]

max_heap = []
for x in arr:
    heapq.heappush(max_heap, -x)

print(max_heap)
