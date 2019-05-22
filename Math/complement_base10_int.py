def bitwiseComplement(self, N):
        """
        https://leetcode.com/problems/complement-of-base-10-integer/
        :type N: int
        :rtype: int
        """
        bin_N = bin(N)
        bin_N = str(bin_N)[2:]
        print bin_N
        complement = ""
        for i in bin_N:
            if i == "0":
                complement += "1"
            elif i == "1":
                complement += "0"
        return int(complement, 2)
