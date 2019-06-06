def exist(self, board, word):
        """
        https://leetcode.com/problems/word-search/
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #Brute Force
        unique = {}
        for inner_lst in board:
            for letter in inner_lst:
                if letter not in unique:
                    unique[letter] = 1
                else:
                    unique[letter] += 1
        print unique
        for letter in word:
            if letter in unique:
                unique[letter] -= 1
            else:
                return False
            if unique[letter] < 0:
                print letter
                print "HELLO"
                return False
        return True
