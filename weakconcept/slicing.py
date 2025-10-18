arr = [10, 20, 30, 40, 50]
# # Get the first three elements

sli = arr[0:3]
print(sli)

# Get the last two elements
last2 = arr[3:5]
print(last2)


# Get elements from index 2 to 4 (inclusive of 2, exclusive of 5)

ind2to4 = arr[1:4]
print(ind2to4)

# Get every second element

every2nd = arr[::2]
print(every2nd, "=======")

# Get the last 3 elements using negative index

last3 = arr[-3:]
print(last3)

# Reverse the list using slicing

rev = arr[::-1]
print(rev, 'rev')

# Get all elements except the first 5 and last 5
arr = list(range(1, 21))
result = arr[5:-5]
print(result)
