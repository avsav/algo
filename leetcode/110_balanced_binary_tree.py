# https://leetcode.com/problems/balanced-binary-tree/description/

""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        heightLeft = self.height(root.left)
        heightRight = self.height(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(heightLeft - heightRight) <= 1


    def height(self, root):
        if not root:
            return 0
        leftHeight = self.height(root.left) 
        rightHeight = self.height(root.right)

        return 1 + max(leftHeight, rightHeight)
"""