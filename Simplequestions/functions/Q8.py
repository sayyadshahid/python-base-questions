# print all alphabates and their asci values

def asci():
    for i in range(ord('A'), ord('z'), +1):
            print(f"{chr(i)}: {i}")

   
# .
asci()