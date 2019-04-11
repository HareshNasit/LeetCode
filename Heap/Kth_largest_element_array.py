def findKthLargest(self, nums, k):
        """
        https://leetcode.com/problems/kth-largest-element-in-an-array/
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """ Check if k > 0
           Create a Max-heap of the elements of nums in O(n).
           Create a while loop for k != 1 and call Extract_Max() in the while loop
           and assign it to a variable declared outside the while loop.
           When k = 1, return the assigned variable.
           Worst case time, O(nlogn).
           Lower bound, when k = len(nums), omega(nlogn)
           Therefore, theta(nlogn).
            
        """
