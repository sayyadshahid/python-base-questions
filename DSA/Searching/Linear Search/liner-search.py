def linearSearch(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x):
            print("element is: ", i)
            return
    print('element is not fount')

print(linearSearch([2,3,4,5,6,7,8], 7))