def letterCombinations(self, digits: str) -> List[str]:
        # Runtime: O(3^n * 4^m) where n = num. of digits with 3 letter
        # mappings and m = num. of digits with 4 letter mappings.
        digit_mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, new_digits):
            if len(new_digits) == 0:
                output_list.append(combination)
            else:
                for letter in digit_mappings[new_digits[0]]:
                    backtrack(combination + letter, new_digits[1:])
        output_list = []
        if digits:
            backtrack("", digits)
        return output_list
