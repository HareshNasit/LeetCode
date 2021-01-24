def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Runtime: O(N*logK) if k < N or O(1) if k = N
        # O(K*logK) for inserting k elements, then O((N-K)*logK) for the remaining elems
        # Total = O(N*logK)
        # Runtime: O(N+k) For Heap and HashMap
        #Case when k = len(nums) 
        if k == len(nums):
            return nums
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        heap = []
        for key, value in freqs.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
                continue
            if heap[0][0] < value:
                heapq.heappop(heap)
                heapq.heappush(heap, (value,key))
        return [elem[1] for elem in heap]
