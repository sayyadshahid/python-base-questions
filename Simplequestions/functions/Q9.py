# factorial of no

def fact(a):
    if a < 0:
        print("factorial is not define for netive number")
    else:
        fact = 1
        for i in range(1, a +1):
            fact = fact * i
    print("factorial of the number is: ", fact)

fact(5)
          