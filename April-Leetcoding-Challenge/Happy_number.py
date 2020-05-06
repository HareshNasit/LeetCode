class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = {}
        str_n = str(n)
        sum_of_digits = 0
        while sum_of_digits != 1:
            sum_of_digits = 0
            for digit in str_n:
                sum_of_digits += int(digit)**2
            str_n = str(sum_of_digits)
            if sum_of_digits not in sum_of_squares:
                sum_of_squares[sum_of_digits] = 1
            else:
                return False

        return True
            
