def searchRange(self, nums, target):
        """
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        points = [-1,-1]
        low = 0
        index = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low += 1
            elif nums[mid] > target:
                high -= 1
            elif nums[mid] == target:
                index = mid
                break
        print mid
        low = 0
        high = index
        lowest = 0
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low += 1
            elif nums[mid] > target:
                high -= 1
            elif nums[mid] == target:
                lowest[0] = mid
                high -= 1
