def lengthOfLastWord(self, s):
        """
        https://leetcode.com/problems/length-of-last-word/submissions/
        :type s: str
        :rtype: int
        """
        split_array = s.split(' ')
        for j in range(len(split_array) - 1, -1, -1):
            if len(split_array[j]) != 0:
                return len(split_array[j])
        return 0
