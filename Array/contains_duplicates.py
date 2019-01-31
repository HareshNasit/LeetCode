#https://leetcode.com/problems/contains-duplicate/submissions/
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        return len(nums) != len(nums_set)
         
        
