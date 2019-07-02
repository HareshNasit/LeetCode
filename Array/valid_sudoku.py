def isValidSudoku(self, board):
        """
        https://leetcode.com/problems/valid-sudoku/submissions/
        :type board: List[List[str]]
        :rtype: bool
        """
        #Idea: Create a method to check if an array of 9 numbers are distinct.
        # Then call the method on all the possible combinations.
        #Rows
        for row in board:
            if self.isUnique(row):
                pass
            else:
                return False
            
        #Columns
        for index in range(9):
            column = []
            for row in board:
                column.append(row[index])
            if self.isUnique(column):
                pass
            else:
                return False
            
        #Squares
        for b in range(3):
            for a in range(3):
                square = []
                for i in range(3): 
                    for j in range(3):
                        square.append(board[3*b + i][3*a + j])
                if not self.isUnique(square):
                    return False
        return True
    
    def isUnique(self,nums):
        nums_set = set()
        for i in nums:
            if i not in nums_set and i != ".":
                nums_set.add(i)
            elif i == ".":
                pass
            else:
                return False
        return True
