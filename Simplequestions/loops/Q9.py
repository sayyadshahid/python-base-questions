# factorial of number 

num = int(input("enter a no"))

if num < 0:
    print("factorial is not define")

else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    print(f"{fact}\n")