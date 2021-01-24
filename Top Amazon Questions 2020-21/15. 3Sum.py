def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 Pointers Approach
        # Runtime: O(n^2)
        # Space: O(n)
        nums.sort() # O(n*logn)
        uniques = []
        # For loop O(n)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            low = i + 1
            high = len(nums) - 1
            # O(n)
            while low < high:
                if nums[low] + nums[high] + nums[i] > 0:
                    high -= 1
                elif nums[low] + nums[high] + nums[i] < 0:
                    low += 1
                else:
                    uniques.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1

        return uniques
