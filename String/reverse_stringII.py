def reverseStr(self, s, k):
        """
        https://leetcode.com/problems/reverse-string-ii/
        :type s: str
        :type k: int
        :rtype: str
        """
        
        s_lst = list(s)
        for i in range(0, len(s), 2*k):
            s_lst[i:i+k] = reversed(s_lst[i:i+k])
        return "".join(s_lst)
