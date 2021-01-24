# Runtime: O(logn) + O(1) = O(logn)
# Space: O(2n)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        if self.max_heap:
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap,num)
        else:
            if not self.min_heap:
                heapq.heappush(self.max_heap,-num)
            else:
                if num <= self.min_heap[0]:
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.min_heap, num)
        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                extract = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -extract)
            else:
                extract = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,extract)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return self.min_heap[0]

# Runtime: O(n) + O(logn) = O(n)
# Space: O(n) For the array
# class MedianFinder:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums = []
#         self.length = 0
#
#     def addNum(self, num: int) -> None:
#         low = 0
#         high = self.length - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if self.nums[mid] == num:
#                 low = mid
#                 break
#             elif self.nums[mid] < num:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         self.nums =  self.nums[:low] + [num] + self.nums[low:]
#         self.length += 1
#     def findMedian(self) -> float:
#         mid = self.length // 2
#         if self.length % 2 == 0:
#             return ((self.nums[mid] + self.nums[mid-1]) / 2.0)
#         return self.nums[mid]

######## BRUTE FORCE ###########################
# Runtime: O(n*logn)
# Space: O(n)
# class MedianFinder:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums = []
#         self.length = 0
#
#     def addNum(self, num: int) -> None:
#         # Runtime: O(1)
#         self.nums.append(num)
#         self.length += 1
#
#     def findMedian(self) -> float:
#         # Runtime: O(n*logn)
#         self.nums.sort()
#         mid = self.length // 2
#         if self.length % 2 == 0:
#             return ((self.nums[mid] + self.nums[mid-1]) / 2.0)
#         return self.nums[mid]
