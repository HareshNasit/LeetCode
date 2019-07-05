def uncommonFromSentences(self, A, B):
        """
        https://leetcode.com/problems/uncommon-words-from-two-sentences/
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words = {}
        for word in A.split(" "):
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
                
        for word in B.split(" "):
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
                
        uncommon_words = []
        for word in words:
            if words[word] == 1:
                uncommon_words.append(word)
        return uncommon_words
        
