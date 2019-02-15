def isHappy(self, n):
        """
        https://leetcode.com/problems/happy-number/
        :type n: int
        :rtype: bool
        """
        #Logic: If the new number generated occurs again, its in an infinite loop.
        sum_squares = n
        set_nums = set()
        while sum_squares != 1 and sum_squares not in set_nums:
            inside_sum = 0
            set_nums.add(sum_squares)
            for i in str(sum_squares):
                inside_sum += int(i)**2
            sum_squares = inside_sum
        return sum_squares == 1
