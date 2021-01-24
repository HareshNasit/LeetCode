class FirstUnique:
    # Runtime: O(K)
    # Space: O(N)
    def __init__(self, nums: List[int]):
        # O(K)
        self.is_unique = {}
        self.nums = []
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # O(K)
        while self.nums and not self.is_unique[self.nums[0]]:
            self.nums.pop(0)

        if self.nums:
            return self.nums[0]
        return -1

    def add(self, value: int) -> None:
        # O(1)
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.nums.append(value)
        else:
            self.is_unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

# Brute Force
# class FirstUnique:
#
#     def __init__(self, nums: List[int]):
#         # O(n)
#         self.freqs = {}
#         self.nums = nums
#         for num in self.nums:
#             if num not in self.freqs:
#                 self.freqs[num] = 1
#             else:
#                 self.freqs[num] += 1
#
#     def showFirstUnique(self) -> int:
#         # O(n)
#         for num in self.nums:
#             if self.freqs[num] == 1:
#                 return num
#         return -1
#
#     def add(self, value: int) -> None:
#         # O(1)
#         if value not in self.freqs:
#             self.freqs[value] = 1
#         else:
#             self.freqs[value] += 1
#         self.nums.append(value)
#
#
# # Your FirstUnique object will be instantiated and called as such:
# # obj = FirstUnique(nums)
# # param_1 = obj.showFirstUnique()
# # obj.add(value)
