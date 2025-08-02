"""
Approach:
Create a queue with the root node initially. Perform BFS on the root node.
On each level, pop the node in the queue and add the value to the sum. If the node has children, append to the queue
When all nodes on each level are popped from the queue, calculate the average value of that level.

Algorithm:
BFS
"""

