def reverseStr(self, s, k):
    """
        :type s: str
        :type k: int
        :rtype: str
        """
            if len(s) <= k:
                reverse = ""
            for i in range(len(s) - 1, -1, -1):
                reverse += s[i]
        return reverse
        else:
            substring = s[:k]
            reverse = ""
