 def isValidSudoku(self, board):
        """
        https://leetcode.com/problems/valid-sudoku/
        :type board: List[List[str]]
        :rtype: bool
        """
        #Idea: Create a method to check if an array of 9 numbers are distinct.
        # Then call the method on all the possible combinations.
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
