class Solution:
    # https://leetcode.com/problems/third-maximum-number/
    def thirdMax(self, nums: List[int]) -> int:
        # Time: O(N)
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')

        for num in set(nums):
            if max(num, first_max) == num:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif max(num, second_max) == num:
                third_max = second_max
                second_max = num
            elif max(num, third_max) == num:
                third_max = num
        if third_max != float('-inf'):
            return third_max
        return first_max
