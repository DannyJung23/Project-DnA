"""
Approach:
Use two pointers starting from the head of each list.
Compare the first nodes (heads) of each list and set the smallest node as the initial prev variable.
While there is a node in both lists, compare the nodes being checked by the pointers and set the smaller node as prev.next
If one list has no more nodes, append the remaining nodes from the other list to the prev list.
"""

# 0ms solution - O(n)

def mergeTwoLists(self, list1, list2):
    if list1 == None and list2 == None:  # if [], []
        return None
    if list1 == None:  # if [], [...]
        return list2
    if list2 == None:  # if [...], []
        return list1

    pointer1 = list1
    pointer2 = list2

    # checking the first node to merge
    if list1.val <= list2.val:
        prev = list1
        merged_head = prev
        pointer1 = pointer1.next
    else:
        prev = list2
        merged_head = prev
        pointer2 = pointer2.next

    # merging until one list has no more node
    while pointer1 and pointer2:
        if pointer1.val <= pointer2.val:
            prev.next = pointer1
            prev = prev.next
            pointer1 = pointer1.next
        else:
            prev.next = pointer2
            prev = prev.next
            pointer2 = pointer2.next

    # appending the remaining nodes
    if pointer1 == None:
        while pointer2:
            prev.next = pointer2
            prev = prev.next
            pointer2 = pointer2.next
    else:
        while pointer1:
            prev.next = pointer1
            prev = prev.next
            pointer1 = pointer1.next
    
    return merged_head


# 0ms solution - O(n)

def mergeTwoLists(self, list1, list2):
    merged_head = [] # ListNode()
    current_node = merged_head

    while list1 and list2:
        if list1.val <= list2.val:
            current_node.next = list1
            current_node = list1
            list1 = list1.next
        else:
            current_node.next = list2
            current_node = list2
            list2 = list2.next
    
    if list1 or list2:
        current_node.next = list1 if list1 else list2
    
    return merged_head.next
