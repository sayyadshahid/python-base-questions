# Q4. Write recursive python program to search element in an array using binary
# search algorithm.

def rec_binary_search(arr, x, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return rec_binary_search(arr, x, low, mid - 1)
    else:
        return rec_binary_search(arr, x, mid + 1, high)
    

a = [10, 30, 20, 50, 30, 60]
a.sort()
result = rec_binary_search(a, 50, 0, len(a) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")