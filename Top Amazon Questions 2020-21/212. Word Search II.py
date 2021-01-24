def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Breadth First Search on all the words
        # Runtime: O(M*N*L)
        # Space: O(M*N)
        result = []
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if word[0] == board[i][j] and self.dfs(board,i,j,0,word):
                        if word not in result:
                            result.append(word)
        return result


    def dfs(self, board, i, j, count, word):
        if count == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or word[count] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = ' '
        exists = self.dfs(board,i+1,j,count+1,word)
        exists = exists or self.dfs(board,i-1,j,count+1,word)
        exists = exists or self.dfs(board,i,j+1,count+1,word)
        exists = exists or self.dfs(board,i,j-1,count+1,word)
        board[i][j] = temp
        return exists
