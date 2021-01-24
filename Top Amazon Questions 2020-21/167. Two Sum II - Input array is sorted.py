def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  Runtime: O(n)
        # Space: O(1)
        low = 0
        high = len(numbers) - 1
        while low <= high:
            curr_sum = numbers[low] + numbers[high]
            if curr_sum == target:
                return [low+1,high+1]
            elif curr_sum > target:
                high -= 1
            else:
                low += 1
        return [-1,-1]
