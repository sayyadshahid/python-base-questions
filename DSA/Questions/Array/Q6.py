# 6) Write python program to implement insertion sort for ascending order of numbers
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

A = [1,3,2,-2,1,-3]
insertion_sort(A)
print(A)