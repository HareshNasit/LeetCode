def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Maintain a max heap to store top K points
        # Runtime: O(N*logK)
        # Space: O(K)
        heap = []
        for point in points:
            distance = (point[0]**2) + (point[1]**2)
            print(distance)
            if len(heap) < K:
                heapq.heappush(heap,(-distance, point))
            elif heap[0][0] < -distance:
                heapq.heappop(heap)
                heapq.heappush(heap,(-distance, point))

        return [i[1] for i in heap]

        # Brute Force
        # Runtime: O(N*logN)
        # Space: O(N)
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]
