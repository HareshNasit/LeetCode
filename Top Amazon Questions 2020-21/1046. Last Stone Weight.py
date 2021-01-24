def lastStoneWeight(self, stones: List[int]) -> int:
        # Runtime: O(nlogn), Space; O(1)
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            elem1 = heapq.heappop(stones)
            elem2 = heapq.heappop(stones)
            if elem1 != elem2:
                heapq.heappush(stones, elem1 - elem2)
                print(stones)
        if len(stones) == 0:
            return 0
        return stones[0]*-1
