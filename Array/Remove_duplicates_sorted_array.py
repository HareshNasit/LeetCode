 def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 0, -1 ):
            print(i)
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)
