# A stack is a LIFO (Last In, First Out) data structure.
# It means — the last item inserted is the first one removed.


stack = []

stack.append(10)
stack.append(20)
stack.append(50)
stack.append(40)
stack.append(30)

print(stack)

stack.pop()

print(stack)

print(stack[-1])

if not stack:
    print(True)
    
else :
    print(False)