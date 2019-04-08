def isPalindrome(self, x):
        """
        https://leetcode.com/problems/palindrome-number/
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_x = str(x)
        return str_x[::-1] == str_x
