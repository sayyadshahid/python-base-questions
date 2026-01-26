class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
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
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
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

    # Delete from Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev
        self.head = self.head.next

        self.head.prev = last
        last.next = self.head

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev
        second_last = last.prev

        second_last.next = self.head
        self.head.prev = second_last

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

    # Display Forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Forward :", end=" ")
        while True:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

    # Display Backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head.prev
        print("Backward:", end=" ")
        while True:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
            if temp == self.head.prev:
                break
        print("(HEAD)")
