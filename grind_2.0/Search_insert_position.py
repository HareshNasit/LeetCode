class Solution:
    # https://leetcode.com/problems/search-insert-position/
    def searchInsert(self, nums: List[int], target: int) -> int:
        # TIme: O(logn) Space: O(1)
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            print(middle)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return left
