def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split_str = str.split(" ")
        count = {}
        index = 0
        if len(pattern) != len(split_str):
            return False
        for word in split_str:
            if word not in count:
                count[word] = pattern[index]
            elif count[word] != pattern[index]:
                return False
            index += 1
        return True
