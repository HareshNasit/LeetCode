def sortArrayByParityII(self, A):
        """
        https://leetcode.com/problems/sort-array-by-parity-ii/submissions/
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None] * len(A)
        even_index = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                result[even_index] = A[i]
                even_index += 2
        odd_index = 1
        for j in range(len(A)):
            if A[j] % 2 == 1:
                result[odd_index] = A[j]
                odd_index += 2
        return result
