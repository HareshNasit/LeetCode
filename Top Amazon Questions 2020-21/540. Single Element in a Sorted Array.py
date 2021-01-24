def singleNonDuplicate(self, nums: List[int]) -> int:
        # TODO: SOLVE IT IN O(logn) USING BINARY SEARCH
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2 # floor division by default
        #     if nums[mid] == nums[mid + 1]:
        #         return nums[mid]
        #     elif ((left - mid) % 2 == 0):
        #         high = mid - 2
        #     else:
        #         low = mid + 2
        # return 0



        # Runtime: O(n), Space: O(1)
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

        # Runtime: O(n), Space: O(n)
        # freqs = {}
        # for num in nums:
        #     if num not in freqs:
        #         freqs[num] = 1
        #     else:
        #         freqs[num] += 1
        # for num in nums:
        #     if freqs[num] == 1:
        #         return num
