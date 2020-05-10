class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Multiplication is costly and so I use addition.
        # Time Complexity O(N), Space Complexity O(1)
        if num == 1:
            return True
        odd_num = 3
        perfect_square = 1
        while perfect_square <= num:
            perfect_square += odd_num
            if perfect_square == num:
                return True
            odd_num += 2
        return False
