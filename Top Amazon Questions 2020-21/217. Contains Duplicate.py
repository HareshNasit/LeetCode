def containsDuplicate(self, nums: List[int]) -> bool:
        # Runtime: O(n)
        # Space: O(n)
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                return True
        return False
