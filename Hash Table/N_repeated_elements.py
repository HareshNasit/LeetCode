def repeatedNTimes(self, A):
        """
        https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/
        :type A: List[int]
        :rtype: int
        """
        set_A = set()
        for i in A:
            if i not in set_A:
                set_A.add(i)
            else:
                return i
            
        #OR
        # dict_A = {}
        # for i in A:
        #     if i not in dict_A:
        #         dict_A[i] = 1
        #     else:
        #         dict_A[i] += 1
        #     if dict_A[i] == (len(A) / 2):
        #         return i
        # return 0
