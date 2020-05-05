class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time complexity O(n), space complexity O(n)
        occurences = {}
        for num in nums:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1
        for num in occurences:
            if occurences[num] == 1:
                return num
