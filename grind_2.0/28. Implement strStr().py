def strStr(self, haystack: str, needle: str) -> int:
        # Runtime: O(N)
        # Space: O(1)
        if len(needle) == 0:
            return 0
        return haystack.find(needle)
