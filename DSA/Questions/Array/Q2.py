# 2) Write python program to implement linear search in recursive manner.
def linear_search_recursive(arr, key, index):
    if index == len(arr):
        return -1

    if arr[index] == key:
        return index
    return linear_search_recursive(arr, key, index + 1)


arr = [10, 25, 30, 45, 60, 75]
key = 45

result = linear_search_recursive(arr, key, 0)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
