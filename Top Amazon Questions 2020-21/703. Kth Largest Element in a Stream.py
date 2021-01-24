class KthLargest:
    # Runtime: O(nlogn)
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums) # Create a min heap O(n)
        self.k = k # k largest element
        # O(nlogn)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # O(logn)
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
