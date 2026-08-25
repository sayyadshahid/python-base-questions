# 11  12  13  14  15   
# 7  8  9  10
# 4  5  6
# 2  3
# 1


rows = 5
n = 1
nums = []

for i in range(1, rows+1):
    row = []
    for j in range(i):
        row.append(n)
        n+= 1
    nums.append(row)

for row in reversed(nums):
    for num in row:
        print(f"{num}", end="  ")
    print(" ")