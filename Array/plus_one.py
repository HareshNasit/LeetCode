def plusOne(self, digits):
        """
        https://leetcode.com/problems/plus-one/submissions/
        
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ""
        for i in digits:
            digits_str += str(i)
        digits_int = int(digits_str) + 1
        new_list = [int(x) for x in str(digits_int)]
        return new_list
