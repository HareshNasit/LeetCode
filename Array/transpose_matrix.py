def transpose(self, A):
        """
        https://leetcode.com/problems/transpose-matrix/submissions/
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #Brute force method
        transpose = []
        for i in range(len(A[0])):
            inside = []
            for j in range(len(A)):           
                inside.append(A[j][i])
            transpose.append(inside)
        return transpose
