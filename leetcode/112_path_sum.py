# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        sum = root.val
        stack = [(root, sum)]

        while stack:
            (node, sum) = stack.pop()
            if not node.left and not node.right and sum == targetSum:
                return True
            if node.left: 
                stack.append((node.left, sum + node.left.val))
            if node.right: 
                stack.append((node.right, sum + node.right.val))
        return False