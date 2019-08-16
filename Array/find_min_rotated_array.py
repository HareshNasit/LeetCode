def findMin(self, nums):
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force
        min_element = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]
        return min_element
