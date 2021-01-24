def romanToInt(self, s: str) -> int:
        # Runtime: O(1) as max possible roman number is 3999, Space: O(1)(constant)
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        int_val = 0
        while i < len(s):
            if i + 1 < len(s)  and roman[s[i]] < roman[s[i+1]]:
                int_val += (roman[s[i+1]] - roman[s[i]])
                i += 2
            else:
                int_val += roman[s[i]]
                i += 1
        return int_val
