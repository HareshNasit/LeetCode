def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    unique = []
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    print(sorted(freq))
    sort=sorted(freq.iteritems(), key = lambda x : x[1], reverse= True)
    output = ""
    for i in sort:
        output += i[0] * i[1]
    return output
