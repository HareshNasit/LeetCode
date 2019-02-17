def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map_s = collections.defaultdict(int)
        for i in s:
            map_s[i] += 1 #Automatically adds any missing value to the dictionary.
        for j in t:
            map_s[j] -= 1
            if map_s[j] == -1:
                return j
