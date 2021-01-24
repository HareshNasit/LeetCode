def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Runtime: O(n), Space: O(1)
        output = []
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            output.append(product)
        output.reverse()
        output.append(1)
        product = 1
        for j in range(len(nums)):
            output[j] *= product
            product *= nums[j]
        return output

        # The below approach can be improved by considering only 1 list
        # Runtime: O(n), Space: O(n)
        # Logic: maintain 2 arrays with left and right products except the num
        # left_sums = [1]
        # right_sums = []
        # product = 1
        # for i in range(len(nums) - 1):
        #     product *= nums[i]
        #     left_sums.append(product)
        # product = 1
        # for j in range(len(nums) - 1, 0, -1):
        #     product *= nums[j]
        #     right_sums.append(product)
        # right_sums.reverse()
        # right_sums.append(1)
        # output = []
        # for i in range(len(nums)):
        #     output.append(left_sums[i] * right_sums[i])
        # return output

        # Brute Force method with 2 loops O(n^2)
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output.append(product)
        # return output
