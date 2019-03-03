def topKFrequent(self, nums, k):
        """
        https://leetcode.com/problems/top-k-frequent-elements/
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        nums_heap = []
        for i in nums:
            if (i) not in nums_dict:
                nums_dict[i] = -1
            else:
                nums_dict[i] -= 1
            print nums_dict
        for number, count in ht.items():
            heapq.heappush(nums_heap, (-1*count, number))
