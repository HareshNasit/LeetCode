class Solution:
    # https://leetcode.com/problems/shuffle-the-array/
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Naivee Method
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[n + i])
        return new_list
