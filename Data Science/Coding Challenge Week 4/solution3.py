def remove_duplicates(head):
    """Takes a LL with non decreasing elements
    Returns a LL with unique elements"""
    if head is None or head.next is None:
        return head
    curr = head
    temp = curr.next
    while temp:
        if curr.val == temp.val:
            temp = temp.next
            continue
        curr.next = temp
        curr = temp
        temp = temp.next
    curr.next = None
    
    return head
