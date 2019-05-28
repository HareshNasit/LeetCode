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
            count = k
            reverse = ""
            while count != 0:
                reverse += s[count - 1]
                count -= 1
            print reverse
            reverse += s[k:]
            return reverse
