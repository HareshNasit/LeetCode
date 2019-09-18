def longestConsecutive(self, nums):
        """
        https://leetcode.com/problems/longest-consecutive-sequence/
        :type nums: List[int]
        :rtype: int
        """
        #Runtime O(NlogN)
        if nums == []:
            return 0
        nums.sort()
        longest_streak = 1
        curr_streak = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_streak += 1
                else:
                    longest_streak = max(curr_streak, longest_streak)
                    curr_streak = 1
        return max(longest_streak, curr_streak)
        #Brute Force: Runtime O(N^3)
        # longest_streak = 0
        # for num in nums:
        #     curr_num = num
        #     curr_streak = 0
        #     while curr_num in nums:
        #         curr_num += 1
        #         curr_streak += 1
        #     longest_streak = max(longest_streak, curr_streak)
        # return longest_streak
