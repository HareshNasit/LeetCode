def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Runtime: O(n), Space: O(1)
        length  = len(s)
        mid = length // 2
        i = 0
        while i < mid:
            s[i], s[length - i - 1] = s[length - i - 1], s[i]
            i += 1
