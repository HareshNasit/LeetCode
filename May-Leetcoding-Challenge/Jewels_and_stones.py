class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for letter in S:
            if letter in J:
                count += 1
        return count
        
