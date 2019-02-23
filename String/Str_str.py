def strStr(self, haystack, needle):
        """ 
        https://leetcode.com/problems/implement-strstr/
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        return -1
