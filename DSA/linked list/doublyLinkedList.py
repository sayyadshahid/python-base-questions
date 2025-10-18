class DoublyLinkedList:
    def __init__(self, data, next= None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)
    
head = tail = DoublyLinkedList(1)

 

def display(head):
    curr = head
    elem = []
    while curr:
        elem.append(str(curr.data))
        curr = curr.next
    print('<->'.join(elem))

display(head)

def add_at_beggening(head, tail, data):
    new_node = DoublyLinkedList(data, next = head)
    head.prev = new_node
    return new_node, tail

head, tail = add_at_beggening(head, tail, 7)
display(head)


def add_at_end(head, tail, data):
    new_node = DoublyLinkedList(data, prev= tail)
    tail.next = new_node
    return head, tail

head, tail = add_at_end(head, tail, 9)
head, tail = add_at_end(head, tail, 29)
head, tail = add_at_end(head, tail, 19)
head, tail = add_at_end(head, tail, 9)
head, tail = add_at_end(head, tail, 9)
head, tail = add_at_end(head, tail, 9)

display(head)

