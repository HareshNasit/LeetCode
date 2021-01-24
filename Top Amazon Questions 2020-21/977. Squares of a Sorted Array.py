def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(nlogn)
        # O(n)
        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # nums.sort() #O(nlogn)
        # return nums

        # Time: O(n) Space: O(n)
        # Merge the 2 squared parts (+ve and -ve nums) using 2 pointers
        n = len(nums)
        first_pos_index = n
        for i in range(n):
            if nums[i] >= 0:
                first_pos_index = i
                break
        for i in range(n):
            nums[i] = nums[i]**2
        output_lst = []
        ptr1 = first_pos_index - 1
        ptr2 = first_pos_index
        while ptr1 >= 0 and ptr2 < n:
            if nums[ptr1] <= nums[ptr2]:
                output_lst.append(nums[ptr1])
                ptr1 -= 1
            else:
                output_lst.append(nums[ptr2])
                ptr2 += 1
        if ptr1 >= 0:
            for i in range(ptr1, -1, -1):
                output_lst.append(nums[i])
        if ptr2 < n:
            output_lst += nums[ptr2:]
        return output_lst
