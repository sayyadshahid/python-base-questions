# read roll no & marks of 3 subject for 3 student display total marks , persentage and display topper 

rollno = input("enter rno of 1st student")

s1 = int(input("enter subject 1 marks"))
s2 = int(input("enter subject 2 marks"))
s3 = int(input("enter subject 3 marks"))

total1 = s1 + s2 + s3
percentage = (total1 / 300) * 100
print("this is your total marks", total1)
print(f"this is your percentage {percentage:.2f}%")

rollno2 = input("enter rno of 2nd student")

s2_1 = int(input("enter subject 1 marks"))
s2_2 = int(input("enter subject 2 marks"))
s2_3 = int(input("enter subject 3 marks"))
# .

total2 = s2_1 + s2_2 + s2_3
percentage2 = (total2 / 300) * 100
print("this is your total marks", total2)
print(f"this is your percentage2 {percentage2:.2f}%")

rollno3 = input("enter rno of 3rd student")

s3_1 = int(input("enter subject 1 marks"))
s3_2 = int(input("enter subject 2 marks"))
s3_3 = int(input("enter subject 3 marks"))

total3 = s3_1 + s3_2 + s3_3
percentage3 = (total3 / 300) * 100
print("this is your total marks", total3)
print(f"this is your percentage3 {percentage3:.2f}%")
 
if total1 > total2 and total1 > total3:
    topper = rollno
    top_score = total1

elif total2 > total1 and total2 > total1:
    topper = rollno2
    top_score = total2

else:
    topper = rollno3
    top_score = total3

print(f"the topper of roll no is {topper} and total marks is {top_score}")