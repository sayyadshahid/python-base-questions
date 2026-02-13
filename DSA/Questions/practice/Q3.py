# Q3. Write Python program to search element in an array using binary search
# algorithm in iterative manner.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

a = [1,2,3,4,5]
print(binary_search(a, 3))
