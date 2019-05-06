 def isPalindrome(self, s):
        """
        https://leetcode.com/problems/valid-palindrome/
        :type s: str
        :rtype: bool
        """
        # Runtime O(n)
        alnum = ""
        for i in s:
            if i.isalnum():
                alnum += i
        alnum = alnum.lower()
        return alnum == alnum[::-1]
