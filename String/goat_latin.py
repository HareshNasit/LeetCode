def toGoatLatin(self, S):
        """
        https://leetcode.com/problems/goat-latin/
        :type S: str
        :rtype: str
        """
        words = S.split(" ")
        print words
        vowels = "aeiouAEIOU"
        for i in range(len(words)):
            if words[i][0] not in vowels:
                words[i] = words[i][1:] + words[i][0] 
            words[i] = words[i] + "ma"
            words[i] += "a"*(i+1)
        return  " ".join(words)
