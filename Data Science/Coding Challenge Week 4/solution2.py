def delete_middle(head):
    """Deletes the Middle Element of a LL.
    If there are even nodes, deletes the second middle element."""
    slow = head
    fast = head
    prev = None

    if head is None or head.next is None:
        head = None
        return head
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    # Now slow is in the middle element
    if prev:
        prev.next = prev.next.next
    return head
