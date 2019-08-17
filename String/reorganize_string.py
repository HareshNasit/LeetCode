def reorganizeString(self, S):
        """
        https://leetcode.com/problems/reorganize-string/767
        :type S: str
        :rtype: str
        """
        letters = {}
        for i in S:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
            # if letters[i] >= ((len(S) + 1) / 2):
            #     return ""
        print letters
        
                
