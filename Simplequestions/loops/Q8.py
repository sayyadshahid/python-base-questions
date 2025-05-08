# check armstrong or not

num = int(input("enter a number"))
temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

if sum == num:
    print("this is a  armstrong number")

else:
    print("not a armstrong number")