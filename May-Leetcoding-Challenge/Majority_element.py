class Solution:
    # Runtime O(N), Space complexity O(N)
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        majority_element = 0
        elem_count = 0
        for num in count:
            if count[num] > elem_count:
                majority_element = num
                elem_count = count[num]
        return majority_element
