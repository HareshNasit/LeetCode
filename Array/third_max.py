def thirdMax(self, nums):
        """
        https://leetcode.com/problems/third-maximum-number/submissions/
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort(reverse = True)
        if len(nums_list) > 2:
            return nums_list[2]
        return nums_list[0]
