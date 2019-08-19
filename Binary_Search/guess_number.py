def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Brute Force
        for i in range(n):
            if guess(i) == 0:
                return i
        return n
        
        #Faster algorithm, using binary search
