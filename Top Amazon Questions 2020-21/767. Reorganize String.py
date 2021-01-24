def reorganizeString(self, S: str) -> str:
        # Runtime: O(N*logA) where A is the num of alphabets used
        # Space: O(A) Storing characters in HashMap and Heap
        freqs = {}
        for c in S:
            if c not in freqs:
                freqs[c] = 1
            else:
                freqs[c] += 1
        max_heap = []
        for key, value in freqs.items():
            heapq.heappush(max_heap, (-value,key))
        reorganized_str = ""
        if len(max_heap) == 1:
            return ""
        while len(max_heap) > 1:
            most_freq = heapq.heappop(max_heap)
            second_most = heapq.heappop(max_heap)
            reorganized_str += most_freq[1]
            reorganized_str += second_most[1]
            if most_freq[0] < -1:
                heapq.heappush(max_heap, (most_freq[0] + 1, most_freq[1]))
            if second_most[0] < -1:
                heapq.heappush(max_heap, (second_most[0] + 1, second_most[1]))
        if len(max_heap) == 1 and max_heap[0][0] < -1:
            return ""
        if len(max_heap) == 1:
            return reorganized_str + max_heap[0][1]
        return reorganized_str
