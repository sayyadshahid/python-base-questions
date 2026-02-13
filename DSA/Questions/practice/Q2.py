# Q2. Write recursive python program to search element in an array using linear
# search algorithm.

def linear_rec_search(arr, x, index):
    if index == len(arr):
        print('element not found')
        return
    
    if arr[index] == x:
        print(index)
        return
    
    linear_rec_search(arr, x, index + 1)



a = [1, 2, 3, 4, 5, 6]
linear_rec_search(a, 6, 0)