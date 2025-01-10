#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_at_begin(self, x):
        node = ListNode(x)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def add_node_at_end(self, x):
        node = ListNode(x)
        if self.head is None:
            self.head = node
        else:      
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def return_node_at_end(self):
        if self.head is None:
            return
        curr = self.head 
        while curr.next:
            curr = curr.next
        return curr

    def return_node_at_pos(self, pos):
        if self.head is None:
            return 
        curr = self.head
        n = 0
        while curr.next and n != pos:
            n += 1
            curr = curr.next
        return curr

    def create_no_cycled_ll(self, h):
        n = len(h)
        for i in range(n):
            self.add_node_at_end(h[i])

    def create_cycled_ll(self, h, pos):
        n = len(h)
        for i in range(n):
            self.add_node_at_end(h[i])   
        node_at_pos = self.return_node_at_pos(pos)
        node_at_end = self.return_node_at_end()
        node_at_end.next = node_at_pos

    def print_no_cycled_ll(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def print_cycled_ll(self, pos):
        node_at_pos = self.return_node_at_pos(pos)
        curr = self.head
        cnt = 0
        while curr:
            if curr == node_at_pos:
                cnt += 1
            print(curr.value)
            curr = curr.next
            if cnt == 2:
                break

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 

    def middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def is_palindrome(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node

        first = self.head
        second = prev
        while second:
            if first.value != second.value:
                return False
            first = first.next
            second = second.next
        return True



    

h1 = [3, 2, 0, -4, 7, 12, 15, 9]
h2 = [1, 2]
h3 = [1, 2, 2, 1]
pos = 1
ll = LinkedList()
ll.create_no_cycled_ll(h3)
ll.reverse_list()
print(ll.is_palindrome())
#ll.create_cycled_ll(h, pos)
#ll.print_cycled_ll(pos)
#ll.print_no_cycled_ll()
#print(ll.has_cycle())
