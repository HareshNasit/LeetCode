def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Runtime: O(n), Space: O(1)
        temp_streak = 0
        highest_streak = 0
        for i in nums:
            if i == 1:
                temp_streak += 1
                highest_streak = max(highest_streak, temp_streak)
            else:
                temp_streak = 0
        return highest_streak
