def guessNumber(self, n):
        """
        https://leetcode.com/problems/guess-number-higher-or-lower/submissions/
        :type n: int
        :rtype: int
        """
        #Brute Force
        # for i in range(n):
        #     if guess(i) == 0:
        #         return i
        # return n
        
        #Faster algorithm, using binary search
        
        left,right = 0,n
        while left <=right:
            mid = (left+right)//2
            if guess(mid) == 0:
                return mid
            else:
                if guess(mid) == 1:
                    left = mid+1
                else:
                    right = mid -1
        return -1
    
