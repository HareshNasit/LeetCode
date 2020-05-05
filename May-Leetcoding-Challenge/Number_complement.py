class Solution:
    def findComplement(self, num: int) -> int:
        complement = ""
        bin_rep = "{0:b}".format(num)
        print(bin_rep)
        for i in bin_rep:
            if int(i) == 0:
                complement += '1'
            else:
                complement += "0"
        print(complement)
        return int(complement, 2)
