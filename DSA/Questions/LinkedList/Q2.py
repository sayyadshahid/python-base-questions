# 2) Write menu driven program for singly circular list using python which contains option
# 1)append 2)insert first 3)insert last 4)insert at given position 5)display 6)search by value 7)delete
# first 8)delete last 9)delete by searching specific value
# ================== NODE CLASS ==================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ================== SINGLY CIRCULAR LINKED LIST ==================
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ---------- APPEND ----------
    def append(self, data):
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

    # ---------- INSERT FIRST ----------
    def insert_first(self, data):
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

    # ---------- INSERT LAST ----------
    def insert_last(self, data):
        self.append(data)

    # ---------- INSERT AT POSITION ----------
    def insert_at_pos(self, data, pos):
        if pos == 1:
            self.insert_first(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while temp.next != self.head and count < pos - 1:
            temp = temp.next
            count += 1

        if count != pos - 1:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # ---------- DISPLAY ----------
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Circular List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

    # ---------- SEARCH ----------
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

    # ---------- DELETE FIRST ----------
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # ---------- DELETE LAST ----------
    def delete_last(self):
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

    # ---------- DELETE BY VALUE ----------
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If head node contains value
        if self.head.data == value:
            self.delete_first()
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                print(f"{value} deleted")
                return
            prev = curr
            curr = curr.next

        print("Value not found")


cll = CircularLinkedList()

while True:
    print("\n--- MENU ---")
    print("1. Append")
    print("2. Insert First")
    print("3. Insert Last")
    print("4. Insert at Position")
    print("5. Display")
    print("6. Search by Value")
    print("7. Delete First")
    print("8. Delete Last")
    print("9. Delete by Value")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        cll.append(int(input("Enter value: ")))

    elif choice == 2:
        cll.insert_first(int(input("Enter value: ")))

    elif choice == 3:
        cll.insert_last(int(input("Enter value: ")))

    elif choice == 4:
        val = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        cll.insert_at_pos(val, pos)

    elif choice == 5:
        cll.display()

    elif choice == 6:
        cll.search(int(input("Enter value to search: ")))

    elif choice == 7:
        cll.delete_first()

    elif choice == 8:
        cll.delete_last()

    elif choice == 9:
        cll.delete_by_value(int(input("Enter value to delete: ")))

    elif choice == 10:
        print("Program exited")
        break

    else:
        print("Invalid choice")
