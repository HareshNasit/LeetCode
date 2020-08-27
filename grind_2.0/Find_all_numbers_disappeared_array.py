class Solution:
    # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(N), Space: O(1)
        for i in range(len(nums)):
            abs_num = abs(nums[i]) - 1
            if nums[abs_num] > 0:
                nums[abs_num] *= -1

        result_lst = []
        for j in range(len(nums)):
            if nums[j] > 0:
                result_lst.append(j + 1)
        return result_lst
        # Time: O(N), Space O(N)
#         occurences = {}
#         for i in nums:
#             if i not in occurences:
#                 occurences[i] = 1

#         result_lst = []
#         for i in range(1,len(nums) + 1):
#             if i not in occurences:
#                 result_lst.append(i)
#         return result_lst
