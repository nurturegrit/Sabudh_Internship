class Node:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next

def max_twin_sum(head):
    if head is None:
        return 0
    if head.next is None:
        return head.val
    # go to the middle element
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse from mid
    prev = None
    while slow:
        after = slow.next
        slow.next = prev
        prev = slow
        slow = after
    
    # go from both ends untill the pointers meet
    max_twin = head.val + prev.val
    while prev and head:
        max_twin = max(max_twin, prev.val + head.val)
        prev = prev.next
        head = head.next
    return max_twin