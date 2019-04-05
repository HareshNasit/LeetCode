def isPowerOfThree(self, n):
        """
        https://leetcode.com/problems/power-of-three/submissions/
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n == 3**(round(math.log(n, 3)))
