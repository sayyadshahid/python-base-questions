class SinglyNode:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
head = SinglyNode(1)
a = SinglyNode(2)
b = SinglyNode(3)
c = SinglyNode(7)


head.next = a
a.next = b
b.next = c

current = head

while current:
    print(current)
    current= current.next


def display(head):
    current= head
    elem = []
    while current:
        elem.append(str(current.data))
        current = current.next

    print('->  '.join(elem))

display(head)