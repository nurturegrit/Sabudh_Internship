def pick_second_last_element(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    return temp.val

