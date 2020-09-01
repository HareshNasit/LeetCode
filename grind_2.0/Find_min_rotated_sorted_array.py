class Solution:
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    def findMin(self, nums: List[int]) -> int:
        # Time Complexity: O(N), Space Complexity: O(1)
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]
