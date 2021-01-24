def isPalindrome(self, x: int) -> bool:
        # Runtime: O(n), Space: O(1)
        # return str(x) == str(x)[::-1] # 1 liner
        if x == 0:
            return True
        if x < 0 or (x != 0 and x % 10 == 0):
            return 0
        reverse_int = 0
        temp = x
        while temp != 0:
            remainder = temp % 10
            reverse_int = reverse_int*10 + remainder
            temp = temp // 10
        if x == reverse_int:
            return True
        return False
