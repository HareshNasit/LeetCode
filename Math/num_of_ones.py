 def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits/submissions/
        :type n: int
        :rtype: int
        """
        h = str(bin(n))
        h = h[2:]
        print(h)
        ones = 0
        for i in h:
            if i == "1":
                ones += 1
        return ones
