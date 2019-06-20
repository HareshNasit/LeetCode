def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    count = {}
    length = 0
    count[1] = 0
    count[0] = 0
    for i in flowerbed:
        count[i] += 1
        length += 1
    print count
    print length/2
    return (count[1] + n) <= (length+1)/2
