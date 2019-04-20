class MinStack(object):

    def __init__(self):
        """
        https://leetcode.com/problems/min-stack/
        initialize your data structure here.
        """
        self.min = []
        self._lst = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self._lst) == 0:
            self.min.append(x)
        elif x < self.min[-1]:
            self.min.append(x)
        self._lst.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        popped = self._lst.pop()
        if self.min[-1] == popped:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._lst[len(self._lst) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
