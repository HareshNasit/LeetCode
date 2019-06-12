def reverseWords(self, s):
        """
        https://leetcode.com/problems/reverse-words-in-a-string/
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reverse_string = ""
        print words
        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                reverse_string += words[i] + " "
        return reverse_string[: len(reverse_string) - 1]
