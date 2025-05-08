# perfect number between 1 to n

def perfect(a):

    for i in range(1, a):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum = sum+j
        
        if sum == i:
            print(i)
    

perfect(10)