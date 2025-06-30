"""
Approach:
Use two pointers slow and fast pointers. The slow pointer moves one node at a time and the fast pointer moves two nodes at a time.
If there is no cycle, the fast pointer will reach None first.
If there is a cycle, the fast pointer will eventually catch up the slow pointer inside the loop.

Algorithm:
Floyd's tortoise and hare (cycle detection for linked lists)
"""

# 31ms solution - O(n)

def hasCycle(self, head):
    if head == None:
        return False
    
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        
        if fast_pointer == slow_pointer:
            return True
        
    return False
