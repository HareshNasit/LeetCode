def majorityElement(self, nums):
        """
        https://leetcode.com/problems/majority-element/submissions/
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
            if nums_dict[i] > (len(nums)//2):
                return i
        return null
