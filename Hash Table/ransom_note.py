 def canConstruct(self, ransomNote, magazine):
        """
        https://leetcode.com/problems/ransom-note/submissions/
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1
        for j in ransomNote:
            if j in mag:
                mag[j] -= 1
            elif j not in mag:
                return False
            if mag[j] == -1:
                return False
        return True
