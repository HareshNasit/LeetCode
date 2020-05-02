# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime O(nlogn) and nlogn API calls in the worst case.
        if n == 1 and isBadVersion(1):
            return n
        low = 1
        high = n
        while low <= high:
            mid = (high+low)//2
            if (isBadVersion(mid)):
                high = mid - 1
            else:
                low = mid + 1
        return low
