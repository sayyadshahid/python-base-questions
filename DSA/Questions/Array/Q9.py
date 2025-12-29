# 9) Write python program to implement bubble sort for descending order of numbers
def bubble_sort(arr):
    n = len(arr)
    for i in range(n -1):
        for j in range(n - i -1):
            if arr[j +1] > arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]


arr = [64, 34, 25, 12, 22, 11, 90]


bubble_sort(arr)

print( arr)
