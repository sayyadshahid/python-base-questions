# 3) Write python program to implement binary search in iterative manner.
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1   


# -------- Main Program --------
arr = [10, 20, 30, 40, 50, 60]
key = 40

result = binary_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
