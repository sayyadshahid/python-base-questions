# Q11. Write Python program to create doubly circular linked list and display it.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node 
            new_node.prev = new_node 
            self.head = new_node
            return
        
        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node
        
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

c = DoubleCircularLinkedList()
c.insert(10)
c.insert(20)
c.insert(30)
c.display()