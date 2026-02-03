# Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None   # init()

    # isEmpty()
    def isEmpty(self):
        return self.top is None

    # isFull() - not applicable in linked list (memory based)
    def isFull(self):
        return False

    # push()
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"{value} pushed into stack")

    # pop()
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        temp = self.top
        self.top = self.top.next
        print(f"Popped element: {temp.data}")

    # peek()
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(f"Top element: {self.top.data}")

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.peek()
s.pop()
s.peek()
