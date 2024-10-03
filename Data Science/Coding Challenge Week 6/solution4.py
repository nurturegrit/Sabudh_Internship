class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge2lists(l1, l2):
    # Merge two sorted linked lists
    dummy = Node()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None
    
    #pairwise merging
    while len(lists) > 1:
        merged_lists = []
        
        # Merge lists in pairs
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge2lists(l1, l2))
        
        # Update the lists to be the merged lists
        lists = merged_lists
    
    return lists[0]


def list_to_nodes(l):
    dummy = Node(0)
    current = dummy
    for val in l:
        current.next = Node(val)
        current = current.next
    return dummy.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


lists = [
    list_to_nodes([1, 4, 5]),
    list_to_nodes([1, 3, 4]),
    list_to_nodes([2, 6])
]

merged_list = merge_k_lists(lists)

print(nodes_to_list(merged_list))