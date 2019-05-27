 def singleNonDuplicate(self, nums):
        """
        https://leetcode.com/problems/single-element-in-a-sorted-array/
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        for i in nums_dict:
            if nums_dict[i] == 1:
                return i
