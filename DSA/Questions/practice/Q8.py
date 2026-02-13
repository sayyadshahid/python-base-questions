# Q8. Write a Python program to sort numbers in descending order using insertion
# sort.

def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


A = [-1, 2, -3, 4, 3, 0, 90, 10]
B = insertion_sort_desc(A)
print(B)
 