# 6. Write a program to count how many times each element appears in a list.

numbers = [1,1,1,3,4,5,6,4,3,3,8]

count= {}

for i in numbers:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
        
        
print(count)