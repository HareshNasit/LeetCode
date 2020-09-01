class Solution:
    # https://leetcode.com/problems/find-peak-element/
    def findPeakElement(self, nums: List[int]) -> int:

        # Runtime: O(logN), Space: O(1)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
        return left

        # Runtime: O(N), Space: O(1)
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return i
        # return len(nums) - 1
