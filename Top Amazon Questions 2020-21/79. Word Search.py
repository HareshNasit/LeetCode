def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and self.dfs(board, i, j, m,n, 0,word):
                    return True
        return False

    def dfs(self,board,i,j,m,n,count,word):
        if count == len(word):
            return True
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = ' '
        exists = self.dfs(board,i+1,j,m,n,count+1,word)
        exists = exists or self.dfs(board,i-1,j,m,n,count+1,word)
        exists = exists or self.dfs(board,i,j+1,m,n,count+1,word)
        exists = exists or self.dfs(board,i,j-1,m,n,count+1,word)
        board[i][j] = temp
        return exists
