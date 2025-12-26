# 4) Write python program to implement binary search in recursive manner.
def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search_recursive(arr, key, low, mid - 1)

    else:
        return binary_search_recursive(arr, key, mid + 1, high)


# -------- Main Program --------
arr = [10, 20, 30,  50, 60]
key = 10

result = binary_search_recursive(arr, key, 0, len(arr) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
