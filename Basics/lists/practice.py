list = [1,2,3,4]
reverse = list[::-1]
print(list)
print(reverse)

# print(list.get("yes", "no"))

# slicing
# [start: stop: jump_index]

print(list[0: 4])
print(list[0:])
print(list[:4])
print(list[::-1])
print(list[0: 4: 2])
print(list[0: 4: 3])

# append: add item add the last 
list.append("hey")
# print(list)


# insert-------> insert(index, item)
list.insert(1, "he")
# print(list)

# extend-----> merge two list

a = [1,2]
b=[2,3]

a.extend(b)
print(a)

# remove-----> remove first ocuurence of x

rem = [1,2,3,4,2]

rem.remove(2)
print(rem)


# pop------------> remove and return item from the index

pop = [1,2,3,4,5,6]

p= pop.pop(1)

print(p)
print(pop)

# return first index of x

index = [1,2,3,42,2]
i = index.index(2)

print(i)

# count------> how many times x appear

count = [1,2,3,4,5,6,1,1]

print(count.count(1))

# sort -----------> sort in assendings 
sort = [1,2,4,2,1,7,65,4]

sort.sort()
print(sort)

# in revese order sorting
sort.sort(reverse=True)
print(sort)

# reverse a list

rev = [1,2,43,5,6,7]
rev.reverse()
print(rev)


# copy
a1 = [1,2,43,2,1]
b1 = a1.copy()
print(b1)


# clear all list

clear = [1,2,43,5]
clear.clear()
print(clear)

x = [1,2,3,4,5]
x.insert(1, 12)
print(len(x))