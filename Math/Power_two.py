def isPowerOfTwo(self, n):
        """
        https://leetcode.com/problems/power-of-two/
        :type n: int
        :rtype: bool
        """
        # If n is a power of 2, (n-1) will be 0...1
        return n > 0 and (n & (n - 1) == 0)
