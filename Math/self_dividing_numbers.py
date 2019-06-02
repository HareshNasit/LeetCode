def selfDividingNumbers(self, left, right):
        """
        https://leetcode.com/problems/self-dividing-numbers/submissions/
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right + 1):
            if self.is_self_dividing(i):
                result.append(i)
        return result
        
    def is_self_dividing(self,num):
        """
        :type num: int
        :rtype: Boolean
        """
        digits = [int(x) for x in str(num)]
        if 0 in digits:
            return False
        for digit in digits:
            if num % digit != 0:
                return False
        return True
            
    
        
