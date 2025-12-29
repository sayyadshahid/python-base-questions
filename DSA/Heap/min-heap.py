import heapq

A = [-4,3,2,4,6,4,1,-10]
heapq.heapify(A)
print(A)

heapq.heappush(A, -3)
print(A)

min = heapq.heappop(A)
print(min, 'min')
print(A, 'min===')


def heapSort(arr):
    heapq.heapify(arr)
    n = len(arr) 
    new_list= [0] * n

    for i in range(n):
        min = heapq.heappop(arr)
        new_list[i] = min
    return new_list


print(heapSort([-3,2,1,4,32,6,-8,6,-5]))
