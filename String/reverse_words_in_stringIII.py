def reverseWords(self, s):
        """
        https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reverse_string = ""
        for word in words:
            temp_word = word[::-1]
            reverse_string += temp_word + " "
        return reverse_string[:len(reverse_string) - 1]
