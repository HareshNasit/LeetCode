 def longestCommonPrefix(self, strs):
        """
        https://leetcode.com/problems/longest-common-prefix/
        :type strs: List[str]
        :rtype: str
        """
        #Idea: Traverse through all the strings, find the intersection one by one.
        if len(strs) == 0:
            return ""
        lcf = strs[0]
        for i in range(1,len(strs)):
            lcf = self.commonPrefix(lcf,strs[i])
            if lcf == "":
                return ""
        return lcf
        
    def commonPrefix(self,str1,str2):
        index = 0
        for i in range(min(len(str1),len(str2))):
            if str1[i] == str2[i]:
                index += 1
            else:
                break
        return str1[:index]
