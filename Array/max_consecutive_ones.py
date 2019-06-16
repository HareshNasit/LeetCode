def findMaxConsecutiveOnes(self, nums):
        """
        https://leetcode.com/problems/max-consecutive-ones/
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for i in nums:
            if i == 0:
                if count >= max_count:
                    max_count = count
                count = 0
            else:
                count += 1
        if count >= max_count:
            return count
        return max_count
