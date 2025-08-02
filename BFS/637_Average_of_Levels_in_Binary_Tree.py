"""
Approach:
Create a queue with the root node initially. Perform BFS on the root node.
On each level, pop the node in the queue and add the value to the sum. If the node has children, append to the queue
When all nodes on each level are popped from the queue, calculate the average value of that level.

Algorithm:
BFS
"""

# 1ms solution - O(n)

def averageOfLevels(self, root):
    average_values = []
    queue = [root]

    while queue:
        num_of_nodes = len(queue)  # number of nodes in the current level
        sum_of_node_vals = 0  # sum of the values of the nodes in the current level

        for i in range(num_of_nodes):
            node = queue.pop(0)
            sum_of_node_vals += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        average_values.append(float(sum_of_node_vals) / num_of_nodes)
    
    return average_values
