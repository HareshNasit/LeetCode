def containsNearbyDuplicate(self, nums, k):
        """
        https://leetcode.com/problems/contains-duplicate-ii/submissions/
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
            elif i - index_dict[nums[i]] <= k:
                return True
            else:
                index_dict[nums[i]] = i
        return False
