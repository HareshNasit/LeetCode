def longestPalindrome(self, s: str) -> str:
        # Runtime: O(N^2)
        # Space: O(N^2)
        palindrom_length = 0
        indexes = []
        grid = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(1,len(grid) + 1):
            grid[i-1][i-1] = 1
            if i != len(grid) and s[i-1] == s[i]:
                grid[i-1][i] = 1
                indexes = [i-1, i]

        for k in range(2,len(s)):
            for i in range(len(s) - 1):
                j = i + k
                if j < len(s) and s[i] == s[j] and grid[i+1][j-1] == 1:
                    grid[i][j] = 1
                    indexes = [i,j]
        if len(indexes) == 0:
            return s[0]
        return s[indexes[0]:indexes[1]+1]
