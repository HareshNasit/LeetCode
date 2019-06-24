def findDuplicates(self, nums):
        """
        https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/
        :type nums: List[int]
        :rtype: List[int]
        """
        unique = set()
        duplicates = []
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                duplicates.append(num)
        return duplicates
