def fib(self, N):
        """
        https://leetcode.com/problems/fibonacci-number/
        :type N: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(N):
            temp = b
            b = a + b
            a = temp
        return a
