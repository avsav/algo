# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [root]

        level = 0
        while queue:
            level += 1
            level_len = len(queue)
            for i in range(level_len):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return level
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
"""