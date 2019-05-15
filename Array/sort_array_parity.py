def sortArrayByParity(self, A):
        """
        https://leetcode.com/problems/sort-array-by-parity/submissions/
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in range(len(A)):
            h = A.pop()
            if h % 2 == 0:
                even.append(h)
            else:
                odd.append(h)
        return even + odd
