def isAnagram(self, s: str, t: str) -> bool:
        # Runtime: O(n)
        # Space: O(1) beacause hash of 26 chars if constant space
        if len(s) != len(t):
            return False
        freqs = {}
        for i in range(len(s)):
            if s[i] not in freqs:
                freqs[s[i]] = 1
            else:
                freqs[s[i]] += 1
        for j in t:
            if j not in freqs:
                return False
            if freqs[j] <= 0:
                return False
            freqs[j] -= 1
        return True


        # # 3 iterations algorithm
        # # Runtime: O(n)
        # # Space: O(1) Hash of 26 chars
        # if len(s) != len(t):
        #     return False
        # s_freqs = {}
        # t_freqs = {}
        # #O(n) iteration
        # for i in s:
        #     if i not in s_freqs:
        #         s_freqs[i] = 1
        #     else:
        #         s_freqs[i] += 1
        # # O(n) iteration
        # for j in t:
        #     if j not in t_freqs:
        #         t_freqs[j] = 1
        #     else:
        #         t_freqs[j] += 1
        # # O(n) iteration
        # for i in s:
        #     if i not in t_freqs or s_freqs[i] != t_freqs[i]:
        #         return False
        # return True
