 def wordPattern(self, pattern, str):
        """
        https://leetcode.com/problems/word-pattern/
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split_str = str.split(" ")
        count = {}
        index = 0
        words_set = []
        if len(pattern) != len(split_str):
            return False
        for letter in pattern:
            print letter
            if letter not in count:
                if split_str[index] not in words_set:
                    count[letter] = split_str[index]
                    words_set.append(split_str[index])
                else:
                    return False
            elif count[letter] != split_str[index]:
                return False
            index += 1
        return True
