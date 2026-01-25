def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    p = arr[-1]
    
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]
    L = quick_sort(L)
    R = quick_sort(R)
    return L + [p] + R

A = [-2,-9, 12 ,4,6]
A = quick_sort(A)

print(A)