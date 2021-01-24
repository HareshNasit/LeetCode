def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Runtime: O(N)
    # Space: O(N)
    nums_dict = {}
    for index in range(len(nums)):
       curr_num = nums[index]
       targ_minus_num = target - curr_num
       if curr_num not in nums_dict:
           nums_dict[curr_num] = index
       if targ_minus_num in nums_dict and (index != nums_dict[targ_minus_num]):
           return [index, nums_dict[targ_minus_num]]
