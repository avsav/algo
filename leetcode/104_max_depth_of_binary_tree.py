# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Rec sol
    if not root:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # Stack sol
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        stack = [(root, depth)]
        max_depth = 0
        while stack:
            (node, depth) = stack.pop()
            if not node.left and not node.right and depth > max_depth:
                max_depth = depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth 
"""