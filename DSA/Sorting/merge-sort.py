def merge_sort(arr):
    n = len(arr)
    
    if n == 1:
        return arr
    m = len(arr) // 2
    L = arr[m:]
    R = arr[:m]
    
    L = merge_sort(L)
    R = merge_sort(R)
    
    L_len = len(L)
    R_len = len(R)
    
    l, r = 0,0
    sortted_arr = [0] * n
    i = 0
    
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sortted_arr[i] = L[l]
            l +=1
        else:
            sortted_arr[i] = R[r]
            r += 1

        i += 1

    while l < L_len:
        sortted_arr[i] = L[l]
        l += 1
        i += 1
    
    while r < R_len:
        sortted_arr[i] = R[r]
        r += 1
        i += 1

    return  sortted_arr

A = [-1, 2, 3, 4, 5, -9, 4, -2]
merge_sort(A)
print(A)