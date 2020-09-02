class Solution:
    # https://leetcode.com/problems/xor-operation-in-an-array/
    def xorOperation(self, n: int, start: int) -> int:
        # Runtime O(N), Space: O(N)
        nums = []
        xor = 0
        for i in range(n):
            value = start + 2*i
            nums.append(value)
            xor ^= value
        return xor
