def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Runtime: O(M*N) For iterating over the original matrix
        # Space: O(M*N) For the matrix
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize the edge cases which are dp[0][i] and dp[i][0] with the same values
        # as the original matrix
        max_length = 0
        for i in range(m):
            dp[i][0] = matrix[i][0]
            if dp[i][0] == "1":
                max_length = 1
        for j in range(n):
            dp[0][j] = matrix[0][j]
            if dp[0][j] == "1":
                max_length = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(int(dp[i-1][j]), int(dp[i-1][j-1]), int(dp[i][j-1])) + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
        return max_length**2
