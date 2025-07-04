"""
Approach:
Implement recursive DFS in-order traversal in the BST which starts at the smallest node and sequentially visiting the next smallest node.
Get the minimum difference between each adjacent node pair.
"""

# 3ms solution - O(n)

def getMinimumDifference(self, root):
    self.min_diff = float('inf')
    self.prev = None

    def dfs(node):
        if node is None:
            return
        
        dfs(node.left)

        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val
        
        dfs(node.right)
    
    dfs(root)
    return self.min_diff
