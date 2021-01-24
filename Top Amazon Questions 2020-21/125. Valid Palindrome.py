def isPalindrome(self, s: str) -> bool:
        # 2 Pointers approach
        # Runtime: O(n)
        # Space: O(1)
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            while ptr1 < ptr2 and not s[ptr1].isalnum():
                ptr1 += 1
            while ptr1 < ptr2 and not s[ptr2].isalnum():
                ptr2 -= 1
            if s[ptr1].lower() != s[ptr2].lower():
                return False

            ptr1 += 1
            ptr2 -= 1

        return True
        # Runtime: O(n)
        # Space: O(n)
        # filtered = ''.join([i.lower() for i in s if i.isalnum()])
        # return filtered[::-1] == filtered
