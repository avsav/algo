class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node

    def pop(self):
        if self.is_empty():
            return None
        tmp = self.first.value
        self.first = self.first.next
        return tmp

    def is_empty(self):
        return self.first is None
    

queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")