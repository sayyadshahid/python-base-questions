# prime no between 1 to 100

print("prime number between 1 to 100")

for i in range(2, 100):
    prime = 1
    for j in range(2, i//2 + 1):
        if(i%j == 0):
            prime = 0
            break
    
    if prime:
        print(f"this is your prime numbers {i}")
