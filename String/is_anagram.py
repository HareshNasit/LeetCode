def isAnagram(self, s, t):
        """
        https://leetcode.com/problems/valid-anagram/
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        letters = {}
        for i in s:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
        for j in t:
            if j in letters:
                letters[j] -= 1
                if letters[j] < 0:
                    return False
            else:
                return False
        return True
