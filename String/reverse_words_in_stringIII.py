 def reverseWords(self, s):
        """
        https://leetcode.com/problems/reverse-words-in-a-string-iii/
        :type s: str
        :rtype: str
        """
        reverse = ""
        for i in range(-1,-1,len(s)):
            reverse += s[i]
        print reverse
