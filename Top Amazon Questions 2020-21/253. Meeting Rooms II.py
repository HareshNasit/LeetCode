def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Runtime: O(nlogn), Space: O(n) for maintaining a min heap
        intervals.sort(key=lambda x: x[0]) # O(nlogn)
        if len(intervals) == 0:
            return 0

        rooms_heap = []
        heapq.heappush(rooms_heap, intervals[0][1])

        for interval in intervals[1:]:
            if rooms_heap[0] <= interval[0]:
                heapq.heappop(rooms_heap)
            heapq.heappush(rooms_heap, interval[1])
        return len(rooms_heap)
