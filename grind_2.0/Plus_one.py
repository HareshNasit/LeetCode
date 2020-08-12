class Solution:
    # Runtime O(N), Space complexity O(1)
    # https://leetcode.com/problems/plus-one/
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            index = len(digits) - i - 1
            print(digits[index])
            if digits[index] + carry == 10:
                carry = 1
                digits[index] = 0
            else:
                digits[index] = digits[index] + carry
                carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits
