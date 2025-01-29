class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.first = None

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node

    def pop(self):
        if self.is_empty():
            return None
        tmp = self.first.value
        self.first = self.first.next
        return tmp

    def is_empty(self):
        return self.first is None
    

stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")