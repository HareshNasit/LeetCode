class Solution:
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TIme O(N), Space O(N)
        occurences = {}
        for index in range(len(nums)):
            if nums[index] not in occurences:
                occurences[nums[index]] = index
            if target - nums[index] in occurences and index != occurences[target - nums[index]]:
                return [occurences[target - nums[index]],index]

        # Time O(N), Space O(N) very similar to the above solution
#         occurences = {}
#         for index in range(len(nums)):
#             if nums[index] not in occurences:
#                 occurences[nums[index]] = index

#         for num in occurences:
#             if target - num in occurences and occurences[num] != occurences[target - num]:
#                 return [occurences[num], occurences[target - num]]
#         return [0,0]
