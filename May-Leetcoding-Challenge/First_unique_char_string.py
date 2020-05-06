class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Runtime O(N) and space complexity O(N)
        letters = {}
        for index in range(len(s)):
            if s[index] not in letters:
                letters[s[index]] = 1
            else:
                letters[s[index]] += 1

        index = 0
        for letter in s:
            if letters[letter] == 1:
                return index
            index += 1
        return -1
