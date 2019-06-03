 def reverseOnlyLetters(self, S):
        """
        https://leetcode.com/problems/reverse-only-letters/submissions/
        :type S: str
        :rtype: str
        """
        str_lst = [i for i in S if i.isalpha()]
        output_str = [] 
        for letter in S:
            if letter.isalpha():
                output_str.append(str_lst.pop())
            else:
                output_str.append(letter)
        return "".join(output_str)
