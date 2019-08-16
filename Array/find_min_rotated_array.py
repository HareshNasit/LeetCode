 def findMin(self, nums):
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force
        # min_element = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i] < min_element:
        #         min_element = nums[i]
        # return min_element
        
        length = len(nums)
        if length == 1:
            return nums[0]
        
        left = 0
        right = length - 1
        if nums[right] > nums[0]:
            return nums[0]
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[0]:
                right = mid - 1
            elif nums[mid] >= nums[0]:
                left = mid + 1
            
            
