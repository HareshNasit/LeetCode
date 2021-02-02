def toLowerCase(self, str: str) -> str:
        # Runtime: O(N)
        # Space: O(1)
        # return str.lower()

        # Runtime: O(N)
        # Space: O(N)
        temp_str = ""
        for s in str:
            if s.isupper():
                temp_str += chr(ord(s) + 32)[0]
            else:
                temp_str += s
        return temp_str
