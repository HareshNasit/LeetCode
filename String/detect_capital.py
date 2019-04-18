def detectCapitalUse(self, word):
        """
        https://leetcode.com/problems/detect-capital/submissions/
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
