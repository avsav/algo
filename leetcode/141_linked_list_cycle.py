# https://leetcode.com/problems/linked-list-cycle/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.h = None

    def add_node_to_end(self, value):
        node = ListNode(value)
        if self.h is None:
            self.h = node       
        curr = self.h
        while curr.next:
            curr = curr.next
        curr.next = node

    def print_ll(self):
        curr = self.h
        while curr is not None:
            print(curr.val)
            curr = curr.next

    def hasCycle(self, head):
        pass

 

head = [3, 2, 0, -4]
pos = 1
obj = Solution()
obj.add_node_to_end(3)
#obj.add_node_to_end(2)
obj.print_ll()
#obj.hasCycle(head)
