# https://leetcode.com/problems/same-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q or p and not q:
            return False

        if not p and not q:
            return True

        qp = [p]
        qq = [q]

        while qp and qq:
            l = max(len(qp), len(qq))
            for i in range(l):
                nqp = qp.pop(0)
                nqq = qq.pop(0)
                if nqp.val != nqq.val:
                    return False
                if nqp.left and not nqq.left or not nqp.left and nqq.left: 
                    return False
                if not nqp.right and nqq.right or nqp.right and not nqq.right:
                    return False
                if nqq.left: qq.append(nqq.left)
                if nqq.right: qq.append(nqq.right)
                if nqp.left: qp.append(nqp.left)
                if nqp.right: qp.append(nqp.right)
        return True
"""