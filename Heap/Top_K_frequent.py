def topKFrequent(self, nums, k):
        """
        https://leetcode.com/problems/top-k-frequent-elements/submissions/
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Runtime O(N)
        nums_dict = {}
        nums_heap = []
        for i in nums:
            if (i) not in nums_dict:
                nums_dict[i] = -1
            else:
                nums_dict[i] -= 1
        for number, count in nums_dict.items():
            heapq.heappush(nums_heap, (count, number))
        output_lst = []
        while k > 0:
            output_lst.append(heapq.heappop(nums_heap)[1])
            k -= 1
        return output_lst
