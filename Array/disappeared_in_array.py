 def findDisappearedNumbers(self, nums):
        """
        https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        set_nums = set(nums)
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                output.append(i)
        return output
