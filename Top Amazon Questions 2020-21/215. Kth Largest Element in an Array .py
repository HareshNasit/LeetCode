def findKthLargest(self, nums: List[int], k: int) -> int:
        # RUntime: O(nlogk) because insert takes logk and n such inserts possible
        # By Default python has min heap
        # Space: O(k)
        max_heap = []
        for num in nums:
            if len(max_heap) < k:
                heapq.heappush(max_heap, num)
            else:
                heapq.heappush(max_heap, num)
                heapq.heappop(max_heap)
        print(max_heap)
        return max_heap[0]


        # Brute Force O(nlogn)
        # nums.sort(reverse=True)
        # return nums[k - 1]
