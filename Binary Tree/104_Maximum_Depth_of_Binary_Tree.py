"""
Approach:
Use recursion on the left subtree and the right subtree.
Find the subtree with the maximum depth using the max() function.
"""

# 0ms solution - O(n)

def maxDepth(self, root):
    if root == None:
        return 0

    left_subtree = 1 + self.maxDepth(root.left)
    right_subtree = 1 + self.maxDepth(root.right)

    return max(left_subtree, right_subtree)


# 3ms solution - O(n)

def maxDepth(self, root):
    if not root:
        return 0

    depth = 1
    depth_left_subtree = 0
    depth_right_subtree = 0

    if (root.left != None):
        depth_left_subtree += self.maxDepth(root.left)

    if (root.right != None):
        depth_right_subtree += self.maxDepth(root.right)

    depth += max(depth_left_subtree, depth_right_subtree)
    return depth
