# 7. Write a program to reverse a list without using the reverse() function.

numbers = [1,2,3,4,5,6,7,8,9]
rev = []

for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])

print(rev)

# or ==========================

rev_num = numbers[::-1]
print(rev_num)
