def evalRPN(self, tokens: List[str]) -> int:
        # Runtime: O(n), Space: O(n)
        stack = []
        for val in tokens:
            if val not in '+-/*':
                stack.append(int(val))
                continue
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                result = 0
                if val == '+':
                    result = val1 + val2
                elif val == '-':
                    result = val2 - val1
                elif val == '*':
                    result = val1*val2
                elif val == '/':
                    result = int(val2 / val1)
                stack.append(result)
        return stack.pop()
