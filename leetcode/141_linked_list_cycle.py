# https://leetcode.com/problems/linked-list-cycle/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.h = None


    def hasCycle(self, head):
        for x in head:
            node = ListNode(x)
            if self.h is None:
                self.h = node

            curr = self.h
            while curr.next:
                curr = curr.next
            curr.next = node
 
            if (curr.val < 0):
                return curr.val








head = [3, 2, 0, -4]
pos = 1
obj = Solution()
print(obj.hasCycle(head))
