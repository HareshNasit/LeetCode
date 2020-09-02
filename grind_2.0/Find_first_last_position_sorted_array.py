class Solution:
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Runtime: O(logN), Space: O(1)
        # Left index
        left = 0
        right = len(nums) - 1
        positions = []
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return [-1,-1]

        positions.append(left)
        # Right Index
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        positions.append(left - 1)
        return positions

        # Time Complexity: O(N), Naivee Algorithm
        # starting_index = -1
        # nums_len = len(nums)
        # for i in range(nums_len):
        #     if nums[i] == target:
        #         starting_index = i
        #         break
        # ending_index = -1
        # for j in range(nums_len - 1, -1, -1):
        #     if nums[j] == target:
        #         ending_index = j
        #         break
        # return [starting_index, ending_index]
