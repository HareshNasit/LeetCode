class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Runtime: O(n)
        # Space: O(n)
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.empty():
            self.queue.append(x)
        else:
            while not self.empty():
                self.stack.append(self.queue.pop())
            self.stack.append(x)
            while len(self.stack) != 0:
                self.queue.append(self.stack.pop())



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
