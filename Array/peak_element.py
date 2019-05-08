def findPeakElement(self, nums):
        """
        https://leetcode.com/problems/find-peak-element/submissions/
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force O(n)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
