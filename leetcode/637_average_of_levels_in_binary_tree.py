# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        avg = []
        
        while queue:
            level_len = len(queue)
            level_sum = 0
            for i in range(level_len):
                node = queue.pop(0)
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            avg.append(level_sum/level_len)
        return avg
"""