# 10) Write python program to implement insertion sort for descending order of numbers
def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] < arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


arr = [64, 34, 25, 12, 22, 11, 90]


insertion(arr)

print( arr)
