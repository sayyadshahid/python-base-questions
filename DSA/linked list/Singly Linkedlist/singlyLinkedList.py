class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at Given Position (1-based index)
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
        temp.next = new_node

    # Delete from Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete by Value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    # Search
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

    # Reverse
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # Display
    def display(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")


sll = SinglyLinkedList()

sll.insert_begin(20)
sll.insert_begin(10)
sll.insert_end(30)
sll.insert_end(40)

sll.display()

sll.insert_at_position(25, 3)
sll.display()
sll.delete_begin()
sll.display()

sll.delete_end()
sll.display()

sll.delete_by_value(25)
sll.display()
sll.search(30)
sll.search(100)

sll.reverse()
sll.display()
