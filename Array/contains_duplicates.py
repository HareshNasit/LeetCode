def containsDuplicate(self, nums):
        """
        https://leetcode.com/problems/contains-duplicate/submissions/
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        return len(nums) != len(nums_set)
         
        
