# 8) Write python program to implement merge sort for ascending order of numbers
def merge_sort(arr):
    n = len(arr)
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])

    l,r = 0, 0
    sortted_idx = [0] * n

    i = 0

    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            sortted_idx[i] = L[l]
            l += 1
        else:
            sortted_idx[i] = R[r]
            r += 1
        i += 1
    while l < len(L):
        sortted_idx[i] = L[l]
        l += 1
        i += 1
    
    while r < len(R):
        sortted_idx[i] = R[r]
        r += 1
        i += 1
    return sortted_idx

A = [1,3,2,-2,1,-3]
A = merge_sort(A)
print(A)