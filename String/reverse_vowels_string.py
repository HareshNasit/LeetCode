 def reverseVowels(self, s):
        """
        https://leetcode.com/problems/reverse-vowels-of-a-string/
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        vowels_s = []
        for i in s:
            if i in vowels:
                vowels_s.append(i)
        index = len(vowels_s) - 1
        new_s = []
        for i in range(len(s)):
            if s[i] in vowels:
                new_s.append(vowels_s[index])
                index -= 1
            else:
                new_s.append(s[i])
        return ''.join(new_s)
        
