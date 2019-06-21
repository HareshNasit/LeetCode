def addToArrayForm(self, A, K):
        """
        https://leetcode.com/problems/add-to-array-form-of-integer/
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        #Brute Force O(N)
        str_A = ""
        for i in A:
            str_A += str(i)
        result = int(str_A) + K
        print result
        output_lst = []
        for i in str(result):
            output_lst.append(int(i))
        return output_lst
    
