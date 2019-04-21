def addDigits(self, num):
    """
    https://leetcode.com/problems/add-digits/
    :type num: int
    :rtype: int
    """
    h = list(str(num))
    s = 0
    for i in h:
        s += int(i)
    if s < 10:
        return s
    return self.addDigits(s)
