def fib(self, n: int) -> int:
        # Runtime: O(2^n)
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        # Runtime: O(n)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev = 1
        curr = 1
        i = 0
        while i < n - 2:
            temp = curr
            curr = curr + prev
            prev = temp
            i += 1
        return curr
