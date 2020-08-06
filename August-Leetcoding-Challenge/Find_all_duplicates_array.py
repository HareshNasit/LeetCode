class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Runtime O(N) and Space complexity O(N)
        duplicates = []
        occurences = {}
        for num in nums:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1
            if occurences[num] == 2:
                duplicates.append(num)
        return duplicates
                
