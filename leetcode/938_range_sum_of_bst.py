# https://leetcode.com/problems/range-sum-of-bst/description/

""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        sum = 0
        li = []
        while queue:
            node = queue.pop(0)
            if node.val >= low and node.val <= high:
                sum += node.val
                li.append(node.val)
            if node.left: 
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return sum#, li
"""