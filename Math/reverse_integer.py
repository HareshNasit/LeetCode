def reverse(self, x):
        """
        https://leetcode.com/problems/reverse-integer/submissions/
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483648:
            return 0
        str_x = str(abs(x))
        reverse_x = ""
        for i in range(len(str_x) - 1,-1, -1):
            reverse_x += str_x[i] 
        result = int(reverse_x)
        if result > 2147483647 or -result < -2147483648:
            return 0
        if x < 0:
            return -result
        return result
