# https://leetcode.com/problems/linked-list-cycle/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.h = None

    def add_node_to_end(self, value):
        node = ListNode(value)
        if self.h is None:
            self.h = node
        else:      
            curr = self.h
            while curr.next:
                curr = curr.next
            curr.next = node

    def return_node_at_end(self):
        if self.h is None:
            return
        curr = self.h
        while curr.next:
            curr = curr.next
        return curr

    def return_node_at_pos(self, pos):
        if self.h is None:
            return 
        curr = self.h
        n = 0
        while curr.next and n != pos:
            n += 1
            curr = curr.next
        return curr

    def create_cycled_list(self, head, pos):
        n = len(head)

        for i in range(n):
            self.add_node_to_end(head[i])
        
        node_at_pos = self.return_node_at_pos(pos)
        node_at_end = self.return_node_at_end()

        node_at_end.next = node_at_pos

        #return node_at_pos.val, node_at_end.val

    def print_ll(self):
        curr = self.h
        while curr:
            print(curr.val)
            curr = curr.next

    def print_cycled_ll(self):
        slow = fast = self.h
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast.val
        return -1

    def hasCycle(self):
        slow = fast = self.h
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False        
 

head = [3, 2, 0, -4]
ll = LinkedList()
ll.create_cycled_list(head, 1)
#print( ll.create_cycled_list(head, 1) )
print(ll.print_cycled_ll())
#ll.hasCycle(head)
#ll.return_node_at_end()
#ll.return_node_at_pos(0)
#ll.print_ll()

