class Solution:
    # https://leetcode.com/problems/missing-number/
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(N), Space: O(1)
        expected_sum = 0
        calculated_sum = 0
        for i in range(1,len(nums) + 1):
            expected_sum += i
            calculated_sum += nums[i - 1]
        return expected_sum - calculated_sum

        # Time: O(N), Space: O(N)
        # occurences = {}
        # for i in nums:
        #     if i not in occurences:
        #         occurences[i] = 1
        # for j in range(len(nums) + 1):
        #     if j not in occurences:
        #         return j
