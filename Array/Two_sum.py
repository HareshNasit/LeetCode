def twoSum(self, nums, target):
        """
        https://leetcode.com/problems/two-sum/submissions/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        indices = []
        alias_nums = nums[0:len(nums)]
        alias_nums.sort()
        while right > left:
            sum_indices = alias_nums[left] + alias_nums[right]
            if sum_indices > target:
                right -= 1
            elif sum_indices < target:
                left += 1
            elif sum_indices == target:
                indices.append(alias_nums[left])
                indices.append(alias_nums[right])
                break
        
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[i] == indices[0]:
                left = i
            if nums[len(nums) - i - 1] == indices[1]:
                right = len(nums) - i - 1
        return [left, right]
