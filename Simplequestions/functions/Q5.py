# check number is prime or not 

def prime(a):
    if a <= 1:
        print("number is undefine ")
    else:
        prime = 1
        for i in range(2, a +1):
            if a % i ==0:
                prime = 0
                break
        if prime:
            print("is a prime no")
        else:
            print("not a prime num")

        return prime
    
prime(20)
# .
        