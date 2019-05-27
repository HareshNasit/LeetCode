def singleNonDuplicate(self, nums):
        """
        https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/
        :type nums: List[int]
        :rtype: int
        """
        
        # for i in range(0,len(nums) - 2,2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # if len(nums) == 0:
        #     return None
        # return nums[-1]
            
        #Brute Force
        # nums_dict = {}
        # for i in nums:
        #     if i not in nums_dict:
        #         nums_dict[i] = 1
        #     else:
        #         nums_dict[i] += 1
        # for i in nums_dict:
        #     if nums_dict[i] == 1:
        #         return i
