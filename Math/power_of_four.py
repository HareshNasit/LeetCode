def isPowerOfFour(self, num):
        """
        https://leetcode.com/problems/power-of-four/submissions/
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        return num == 4**(round(math.log(num, 4)))
