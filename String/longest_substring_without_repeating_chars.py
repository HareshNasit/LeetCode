def lengthOfLongestSubstring(self, s):
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        :type s: str
        :rtype: int
        """
        substring = []
        longest_substring_len = 0
        for i in s:
            if i not in substring:
                substring.append(i)
            else:
                longest_substring_len = max(longest_substring_len, len(substring))
                substring = substring[substring.index(i) + 1:]
                substring.append(i)
        return max(longest_substring_len, len(substring))
