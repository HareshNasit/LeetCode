  def __init__(self):
        """
        initialize your data structure here.
        """
        self._lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._lst.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self._lst.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._lst[len(self._lst) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self._lst)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
