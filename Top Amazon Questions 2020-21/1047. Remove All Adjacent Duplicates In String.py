def removeDuplicates(self, S: str) -> str:
        # Runtime: O(n)
        # Space: O(n - d) where d = num. of duplicates
        stack = []
        for s in S:
            if len(stack) == 0:
                stack.append(s)
            elif stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
