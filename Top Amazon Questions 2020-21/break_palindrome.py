def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ''
        for i, char in enumerate(palindrome):
            if char != 'a' and i != n//2:
                return palindrome[:i] + 'a' + palindrome[i+1:]
            elif char == 'a' and i == n - 1:
                return palindrome[:-1] + 'b'
