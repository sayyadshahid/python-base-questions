# Q7. Write Python program to sort numbers in ascending order using insertion sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1] 
                break
    return arr

A = [-1,2,-3,4,3,0,90,10]
B= insertion_sort(A)
print(B)