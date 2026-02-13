# Q6. Write Python program to sort elements in descending order using bubble sort.

def bubble_sort_desc(arr):
    n = len(arr)
    flag =  True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

A = [-1,2,-3,4,3,0,90,10]
B= bubble_sort_desc(A)
print(B)