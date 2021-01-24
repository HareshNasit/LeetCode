def isValid(self, s: str) -> bool:
        # Runtime: O(n), Space: O(n)
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            else:
                if len(stack) == 0 or stack.pop() != i:
                    return False
        return len(stack) == 0
