class Solution:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: List[int]) -> bool:

        # return len(nums) - len(set(nums)) != 0

        # Runtime O(N) and Space Complexity O(N)
        unique = {}
        for elem in nums:
            if elem not in unique:
                unique[elem] = 1
            else:
                return True
        return False
