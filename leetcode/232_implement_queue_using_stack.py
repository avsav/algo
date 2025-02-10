# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        front = self.output.pop()
        return front

    def peek(self) -> int:
        front = self.pop()
        self.output.append(front)
        return front
        
    def empty(self) -> bool:
        return not self.input and not self.output 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
"""
myQueue.push(1) 
myQueue.push(2) 
myQueue.push(3) 
myQueue.push(4) 
print(myQueue.pop())
myQueue.push(5)
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
"""