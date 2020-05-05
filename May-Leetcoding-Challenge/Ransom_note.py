class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_count = {}
        for i in magazine:
            if i not in letters_count:
                letters_count[i] = 1
            else:
                letters_count[i] += 1
        for letter in ransomNote:
            if letter in letters_count and letters_count[letter] > 0:
                letters_count[letter] -= 1
            else:
                return False
        return True
