def findErrorNums(self, nums):
        """
        https://leetcode.com/problems/set-mismatch/submissions/
        :type nums: List[int]
        :rtype: List[int]
        """
        unique = set()
        duplicate = 0
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
            else:
                duplicate = nums[i]
        print duplicate
        result = [duplicate]
        for i in range(1,len(nums) + 1):
            if i not in unique:
                result.append(i)
        return result
