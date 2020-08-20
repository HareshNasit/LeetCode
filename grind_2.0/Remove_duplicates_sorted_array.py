class Solution:
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time COmplexity O(N), Space Complexity O(1)
        pointer = 0
        for i in range(1,len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1
