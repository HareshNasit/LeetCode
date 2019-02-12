def singleNumber(self, nums):
        """
        https://leetcode.com/problems/single-number/submissions/
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1 
            else:
                counter[i] = 1
        for j in counter:
            if counter[j] == 1:
                return j
        return 0
