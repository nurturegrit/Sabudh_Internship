class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_LL_as_nums(l1, l2):
    dummy = Node()
    curr = dummy
    carry = 0

    #Traverse both lists and find sum
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total//10
        total %= 10

        curr.next = Node(total)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

