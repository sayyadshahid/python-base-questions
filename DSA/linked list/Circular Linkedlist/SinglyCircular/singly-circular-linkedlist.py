class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Delete from Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next

        prev.next = self.head

    # Search
    def search(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 1
        while True:
            if temp.data == value:
                print(f"{value} found at position {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        print("Value not found")

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Circular List:", end=" ")
        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")
