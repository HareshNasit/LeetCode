def search(self, nums, target):
        """
        https://leetcode.com/problems/binary-search/solution/
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low += 1
            elif nums[mid] > target:
                high -= 1
        return -1
