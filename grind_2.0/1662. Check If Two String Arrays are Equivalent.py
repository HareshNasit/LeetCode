def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    # Runtime: O(N) for traversing both the words
    # Space: O(N) for storing both the words
    str1 = ''.join(word1)
    str2 = ''.join(word2)
    return str1 == str2
