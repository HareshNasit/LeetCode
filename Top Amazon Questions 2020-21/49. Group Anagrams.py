def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Runtime: O(N*K)
        # Space: O(N*K)
        groups = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tup = tuple(count)
            if tup not in groups:
                groups[tup] = [s]
            else:
                groups[tup].append(s)
        return groups.values()

        # Runtime: O(N*K*logK) where K is max len of string in strs and n is len(strs)
        # Space: O(N*K) for storing string occurences and groups
        # groups = {}
        # # O(N)
        # for s in strs:
        #     s_sort = tuple(sorted(s)) #O(KlogK)
        #     if s_sort not in groups:
        #         groups[s_sort] = [s]
        #     else:
        #         groups[s_sort].append(s)
        # return groups.values()
