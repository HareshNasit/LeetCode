def heightChecker(self, heights):
        """
        https://leetcode.com/problems/height-checker/submissions/
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        unsorted = heights[:]
        # for i in heights:
        #     print heights[i]
        #     unsorted.append(heights[i])
        heights.sort()
        for j in range(len(heights)):
            if heights[j] != unsorted[j]:
                count += 1
        return count
