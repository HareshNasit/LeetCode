def removeElement(self, nums, val):
        """
        https://leetcode.com/problems/remove-element/submissions/
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)
