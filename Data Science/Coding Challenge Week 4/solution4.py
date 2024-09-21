def reverse_linked_list(head):
        """Function to Reverse the Linked List"""
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev