class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #   Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    #  Insert at End
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

    #  Insert at Given Position (1-based index)
    def insert_at_position(self, data, pos):
        if pos == 1:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    #  Delete from Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    #   Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    #   Delete by Value
    def delete_by_value(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Value not found")

    #   Search
    def search(self, value):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == value:
                print(f"{value} found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print("Value not found")

    #  Display Forward
    def display_forward(self):
        temp = self.head
        print("Forward :", end=" ")
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("NULL")

    #   Display Backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("Backward:", end=" ")
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("NULL")


dll = DoublyLinkedList()

dll.insert_begin(20)
dll.insert_begin(10)
dll.insert_end(30)
dll.insert_end(40)

dll.display_forward()
dll.display_backward()

dll.insert_at_position(25, 3)
dll.display_forward()

dll.delete_begin()
dll.display_forward()

dll.delete_end()
dll.display_forward()

dll.delete_by_value(25)
dll.display_forward()

dll.search(30)
dll.search(100)
