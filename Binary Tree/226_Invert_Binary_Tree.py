"""
Approach:
Swap the left and right children of all nodes in the original tree.
Use recursion on the left and right subtrees and swap from the bottom.
"""

# 0ms solution - O(n)

def invertTree(self, root):
    if root is None:
        return None
    
    # bottom-up recursion
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)

    # swap the children
    root.left = right
    root.right = left

    return root
