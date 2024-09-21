class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_ll_elements_as_digits(head1, head2):
    def reverse_linked_list(head):
        """Returns Reversed LL and Length of LL"""
        prev = None
        curr = head
        len = 0
        while curr:
            len += 1
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev, len
    def add_two_nodes(node1, node2_val, carry):
        """return carry"""
        total = node1.val + node2_val + carry
        node1.val = total % 10
        return total//10
    
    if head1 is None or head2 is None:
        return head1 or head2
    # Reverse both lists
    head1, l1 = reverse_linked_list(head1)
    head2, l2 = reverse_linked_list(head2)

    if l1 > l2:
        temp1, temp2 = head1, head2
    else:
        temp1, temp2 = head2, head1
    # Add node vals of both linked lists
    carry = False
    while temp1 and temp2:
        prev = temp1
        carry = add_two_nodes(temp1, temp2.val, carry)
        temp1, temp2 = temp1.next, temp2.next
    if temp1 and carry:
        prev = temp1
        carry = add_two_nodes(temp1, 0, carry)
        temp1 = temp1.next
    if carry:
        prev.next = Node(carry)

    if l1 > l2:
        head1, l = reverse_linked_list(head1)
        return head1
    else:
        head2, l = reverse_linked_list(head2)
        return head2
    
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

head1 = Node(5, Node(6, Node(3)))  # 563
head2 = Node(8, Node(4, Node(2)))  # 842

# Adding the numbers
result = add_ll_elements_as_digits(head1, head2)

# Printing the result
print_linked_list(result)