def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Runtime: O(N)
        # Space: O(N - k + 1) + O(k) for the deque
        if len(nums) == 0 or k > len(nums):
            return []

        result = [] # Size n - k + 1
        queue = deque([])

        i = 0
        while i < len(nums):
            # Checking deque from the left
            if queue and queue[0] == i - k:
                queue.popleft()

            # Checking nums < nums[i] from the right
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # Append the new element
            queue.append(i)

            if i >= k - 1: # i is atleast k
                result.append(nums[queue[0]])
            i += 1
        return result


        # Brute Force
        # Runtime: O(n*k)
        # Space: O(n)
        # max_nums = []
        # for i in range(len(nums) - k+1):
        #     max_nums.append(max(nums[i:i+k]))
        # return max_nums
