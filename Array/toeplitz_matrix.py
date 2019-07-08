def isToeplitzMatrix(self, matrix):
        """
        https://leetcode.com/problems/toeplitz-matrix/solution/
        :type matrix: List[List[int]]
        :rtype: bool
        """
        #Enumerate is used to track a counter as well as the value in the array.
        diagnols = {}
        for r, row in enumerate(matrix,1):
            for c, value in enumerate(row,1):
                if r - c not in diagnols:
                    diagnols[r-c] = value
                elif diagnols[r - c] != value:
                    return False
        return True
