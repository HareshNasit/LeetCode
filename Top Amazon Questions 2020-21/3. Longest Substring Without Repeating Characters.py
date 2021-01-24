def lengthOfLongestSubstring(self, s: str) -> int:
        # Runtime: O(n), Space: O(n)
        streak = 0
        start = 0
        index_dict = {}
        for i, val in enumerate(s):
            if s[i] in index_dict:
                start = max(index_dict[val], start)
            index_dict[val] = i + 1
            streak = max(streak, i - start + 1)
        return streak
