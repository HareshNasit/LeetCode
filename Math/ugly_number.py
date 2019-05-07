def isUgly(self, num):
        """
        https://leetcode.com/problems/ugly-number/submissions/
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        while num != 0:
            if num == 1:
                return True
            elif num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                return False
        return False
