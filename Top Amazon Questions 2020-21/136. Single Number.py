def singleNumber(self, nums: List[int]) -> int:
        # Runtime: O(n)
        # Space: O(1)
        # Logic: XOR of a and 0 = a, a and a = 0, at the end
        # we will be left with the single number
        a = 0
        for i in nums:
            a ^= i
        return a
        # Runtime: O(n)
        # Space: O(n) Hashmap
        # freqs = {}
        # for num in nums:
        #     if num not in freqs:
        #         freqs[num] = 1
        #     else:
        #         freqs[num] += 1
        # for num in freqs:
        #     if freqs[num] == 1:
        #         return num
        # return 0
