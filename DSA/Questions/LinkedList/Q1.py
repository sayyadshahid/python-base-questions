# 1) Write menu driven program for singly list using python which contains option
# append 2)insert first 3)insert last 4)insert at given position 5)display 6)search by value 7)delete
# first 8)delete last 9)delete by searching specific value
# ================== NODE CLASS ==================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ================== SINGLY LINKED LIST ==================
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # ---------- APPEND ----------
    def append(self, data):
        self.insert_end(data)

    # ---------- INSERT AT BEGIN ----------
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ---------- INSERT AT END ----------
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # ---------- INSERT AT POSITION ----------
    def insert_at_pos(self, data, pos):
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

    # ---------- DELETE FIRST ----------
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # ---------- DELETE LAST ----------
    def delete_last(self):
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

    # ---------- DELETE BY VALUE ----------
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print(f"{value} deleted")
            return

        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(f"{value} deleted")
                return
            temp = temp.next

        print("Value not found")

    # ---------- SEARCH ----------
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

    # ---------- DISPLAY ----------
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# ================== MENU ==================
sll = SinglyLinkedList()

while True:
    print("\n--- MENU ---")
    print("1. Append")
    print("2. Insert First")
    print("3. Insert Last")
    print("4. Insert at Given Position")
    print("5. Display")
    print("6. Search by Value")
    print("7. Delete First")
    print("8. Delete Last")
    print("9. Delete by Searching Value")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sll.append(int(input("Enter value: ")))

    elif choice == 2:
        sll.insert_begin(int(input("Enter value: ")))

    elif choice == 3:
        sll.insert_end(int(input("Enter value: ")))

    elif choice == 4:
        val = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        sll.insert_at_pos(val, pos)

    elif choice == 5:
        sll.display()

    elif choice == 6:
        sll.search(int(input("Enter value to search: ")))

    elif choice == 7:
        sll.delete_first()

    elif choice == 8:
        sll.delete_last()

    elif choice == 9:
        sll.delete_by_value(int(input("Enter value to delete: ")))

    elif choice == 10:
        print("Program exited")
        break

    else:
        print("Invalid choice")
