nums = [3,0,1]
n_sum = 0
nums_sum = 0
for i in range(len(nums)):
    n_sum += i
    nums_sum += nums[i]
n_sum += len(nums)
print (n_sum - nums_sum)
