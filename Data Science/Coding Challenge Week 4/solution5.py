class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_1_to_ll(head):
    # Function to reverse the list
    def reverse_linked_list(head):
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
    
    def add_one(node):
        # adds one to new head and returns carry
        carry = False
        node.val += 1
        if node.val == 10:
            node.val = 0
            carry = True
        return carry
    
    head = reverse_linked_list(head) # new head
    temp = head 
    carry = add_one(temp)

    while carry and temp.next:
        temp = temp.next
        carry = add_one(temp)
    if carry:
        new_node = Node(val=1)
        temp.next = new_node
    
    head = reverse_linked_list(head)
    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# Example usage:
head = Node(9, Node(9, Node(9)))
head = add_1_to_ll(head)
print_linked_list(head)


    


