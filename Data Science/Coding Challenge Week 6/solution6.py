class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # Start with the head of the list
    current = head
    
    # Traverse the list
    while current and current.next:
        # If the current node's value is equal to the next node's value
        if current.val == current.next.val:
            # Skip the next node
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
    
    # Return the modified list
    return head