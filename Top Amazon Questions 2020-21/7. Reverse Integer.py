def reverse(self, x: int) -> int:
        # Runtime: O(1), Space: O(1)
        if x < 0:
            y = str(x)[:0:-1]
            y = '-' + y
            return 0 if int(y) < -2147483647 else int(y)
        else:
            y = str(x)[::-1]
            return 0 if int(y) > 2147483647 else int(y)
