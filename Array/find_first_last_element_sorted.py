def searchRange(self, nums, target):
        """
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Brute Force, O(N)
        points = [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                points[0] = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                points[1] = j
                break
        return points
