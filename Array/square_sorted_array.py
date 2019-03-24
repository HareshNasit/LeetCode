def sortedSquares(self, A):
        """
        https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
        :type A: List[int]
        :rtype: List[int]
        """
        h = [i*i for i in A]
        h.sort()
        return h 
