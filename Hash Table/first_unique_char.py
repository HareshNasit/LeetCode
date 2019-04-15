def firstUniqChar(self, s):
        """
        https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
        :type s: str
        :rtype: int
        """
        letters = {}
        count = 0
        for i in s:
            if i not in letters:
                letters[i] = 1
                count += 1
            else:
                letters[i] += 1
        for j in range(len(s)):
            if letters[s[j]] == 1:
                return j
        return -1
