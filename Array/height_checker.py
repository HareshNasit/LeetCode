def heightChecker(self, heights):
        """
        https://leetcode.com/problems/height-checker/
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        unsorted = []
        for i in heights:
            unsorted.append(heights[i])
        heights.sort()
        for j in range(len(heights)):
            if heights[j] != unsorted[j]:
                count += 1
        return count
