def arrayPairSum(self, nums):
        """
        https://leetcode.com/problems/array-partition-i/submissions/
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total_sum = 0
        index = 0
        while index < len(nums) - 1:
            total_sum += min(nums[index], nums[index + 1])
            index += 2
        return total_sum
