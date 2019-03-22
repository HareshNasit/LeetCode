def moveZeroes(self, nums):
        """
        https://leetcode.com/problems/move-zeroes/
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                if i != non_zero_index:
                    nums[i] = 0
                non_zero_index += 1
