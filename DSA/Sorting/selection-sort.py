A =  [-1,2,3,4,5,-9,4,-2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_inx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]
           

selection_sort(A)
print(A)