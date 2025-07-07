"""
Approach:
Use two pointers starting from the head of each list.
Compare the first nodes (heads) of each list and set the smallest node as the initial prev variable.
While there is a node in both lists, compare the nodes being checked by the pointers and set the smaller node as prev.next
If one list has no more nodes, append the remaining nodes from the other list to the prev list.
"""