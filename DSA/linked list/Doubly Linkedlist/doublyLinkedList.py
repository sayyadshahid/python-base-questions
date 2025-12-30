
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("NULL")
        
dll = DoublyLinkedList()

dll.insert_begin(20)
dll.insert_begin(10)
dll.insert_end(30)
dll.insert_end(40)

dll.display_forward()