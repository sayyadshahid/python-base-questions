def linear_search(arr, x):
    a = len(arr)
    for i in range(1, a):
        if arr[i] == x:
            return i
    print('number is not found')
a = [1,2,3,4,5,6]

print(linear_search(a, 6))