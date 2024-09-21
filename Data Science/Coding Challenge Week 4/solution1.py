def print_middle(head):
    """Prints Middle of the Linked List"""
    if head is None:
        print(None)
        return
    
    if head.next is None:
        print(head.val)
        return
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(slow.val)
    return