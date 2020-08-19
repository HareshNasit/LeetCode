class Solution:
    # https://leetcode.com/problems/remove-element/submissions/
    def removeElement(self, nums: List[int], val: int) -> int:
        # Runtime: O(N), Space Complexity: O(1)
        # USE POINTERS FOR IN PLACE QUESTIONS
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer

        # Brute Force O(N^2)
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 temp = i + 1

#                 while temp < len(nums) and nums[temp] == val:
#                     temp += 1
#                 if temp < len(nums):
#                     count += 1
#                     nums[temp], nums[i] = nums[i], nums[temp]
#             else:
#                 count += 1
        # return count
