class Solution:
    # Time Complexity O(N), Space Complexity O(1)
    # https://leetcode.com/problems/max-consecutive-ones/submissions/
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        temp_count = 0
        for i in nums:
            if i == 1:
                temp_count += 1
            elif i == 0:
                max_num = max(max_num,temp_count)
                temp_count = 0
        return max(temp_count,max_num)
