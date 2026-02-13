# Q9. Write Python program to create singly linked list and display it.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SignlyLinkedList:
    def __init__(self):
        self.head = None 

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" => ")
            temp = temp.next
        print('NULL')
c = SignlyLinkedList()
c.insert(1)
c.insert(12)
c.insert(10)
c.display()