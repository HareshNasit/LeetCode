def compress(self, chars):
        """
        https://leetcode.com/problems/string-compression/
        :type chars: List[str]
        :rtype: int
        """
        h = {}
        for i in chars:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        print h
        char = []
#         for i in h:
#             print i
#             char.append(i)
#             count = str(h[i])
#             print count
#             char.append(count)
#         chars = char
#         return len(chars)
        
        
