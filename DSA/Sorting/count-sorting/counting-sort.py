def countng_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    maxx = max(arr)
    counting = [0] * (maxx + 1)
    i =0 
    for x in arr:
        counting[x] += 1
        
    for c in range(maxx + 1):
        while counting[c] > 0: 
            arr[i] = c
            i += 1
            counting[c] -= 1
    return arr
            

A = [12 ,4,6]
A = countng_sort(A)

print(A)
            