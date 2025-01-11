# https://leetcode.com/problems/remove-linked-list-elements/description/

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.val == val:
            curr = curr.next
        head = curr

        while curr and curr.next:
            next_node = curr.next
            while next_node and next_node.val == val:
                next_node = next_node.next
            curr.next = next_node
            curr = curr.next
        return head
"""