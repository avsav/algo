# https://leetcode.com/problems/diameter-of-binary-tree/description/

""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, max_diam=0):
        self.max_diam = max_diam

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr_diam = self.maxDepth(root.left) + self.maxDepth(root.right)
        self.max_diam = max(curr_diam, self.max_diam)
        if root.left:
            self.diameterOfBinaryTree(root.left)
        if root.right:
            self.diameterOfBinaryTree(root.right)
        return self.max_diam

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
"""