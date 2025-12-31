# 1) Write menu driven program for singly list using python which contains option
# append 2)insert first 3)insert last 4)insert at given position 5)display 6)search by value 7)delete
# first 8)delete last 9)delete by searching specific value

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
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
    
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            self.insert_begin(data)
            return
        
        temp = self.head
        count = 1

        while temp and count < pos -1:
            temp = temp.next
            count += 1

        if temp is None:
                print("Invalid Position")
                return
        
        new_node.next = temp.next
        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print('list is empty')
            return
        
        self.head = self.head.next
    
    def delete_end(self):
        if self.head is None:
            print('list is empty')
            return
        
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None
    def delete_pos(self, pos):
        if pos == 1:
            self.delete_first()
            return
        
        temp = self.head
        count = 1

        while temp and count < pos -1:
            temp = temp.next
            count += 1
        
        if self.head is None:
            print('invalid list')
            return
        
        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
        
        
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

ddl = SinglyLinkedList()
ddl.insert_begin(12)
ddl.insert_begin(12)
# ddl.insert_end(1002)
ddl.insert_at_pos(1002,1)
# ddl.delete_first()
# ddl.delete_end()
ddl.delete_pos(1)
ddl.display()
