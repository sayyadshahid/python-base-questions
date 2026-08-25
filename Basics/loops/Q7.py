# check no is palidrome or not


elem = input("enter a number or string for check palidrome or not")

reverse_elem = elem[::-1]

if(elem == reverse_elem):
    print("this is palidrome")

else:
    print("this is not pelidrome")