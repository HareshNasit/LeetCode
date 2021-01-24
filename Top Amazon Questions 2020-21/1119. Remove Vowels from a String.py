def removeVowels(self, s: str) -> str:
        # Runtime O(n), Space: O(1)
        vowels = "aeiou"
        for letter in s:
            if letter in vowels:
                s = s.replace(letter, '')
        return s

        # Runtime: O(n), Space: O(n)
        # filtered_str = ""
        # vowels = "aeiou"
        # for letter in s:
        #     if letter not in vowels:
        #         filtered_str += letter
        # return filtered_str
