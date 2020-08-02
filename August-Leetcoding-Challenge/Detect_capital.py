import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch("[A-Z]*|[a-z]*|[A-Z][a-z]*", word)
