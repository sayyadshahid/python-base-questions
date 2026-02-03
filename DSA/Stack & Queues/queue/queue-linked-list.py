# Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None   # init()
        self.rear = None

    # isEmpty()
    def isEmpty(self):
        return self.front is None

    # enqueue()
    def enqueue(self, value):
        new_node = Node(value)

        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"{value} enqueued into queue")

    # dequeue()
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Dequeued element: {temp.data}")

    # peek()
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(f"Front element: {self.front.data}")

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.dequeue()
q.peek()
