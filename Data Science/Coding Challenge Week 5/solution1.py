class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_at_front(head, val):
    new_node = Node(val, head)
    head = new_node
    return head


head = Node(9, Node(10, None))

head = add_at_front(head, 8)

print(head.val)