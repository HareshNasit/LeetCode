def rotateString(self, A, B):
        """
        https://leetcode.com/problems/rotate-string/submissions/
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == 0 and len(B) == 0:
            return True
        length = len(A)
        count = 0
        temp_A = A
        while count < length:
            if temp_A == B:
                return True
            temp_A = temp_A[1:] + temp_A[0]
            count += 1
        return False
