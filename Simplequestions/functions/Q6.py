# prime no between 1 to 100

def prime(a):
    for i in range(2, a+1):
        prime = 1

        for j in range(2, i//2+1):
            if i % j==0:
                prime = 0
                break
        if prime:
            print(i)

  

prime(200)