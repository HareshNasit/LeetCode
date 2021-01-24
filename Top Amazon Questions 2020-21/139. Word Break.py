def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Dynamic Programming
        # Runtime: O(n*w) where n is len(s) and w is the len(wordDict)
        # Space: O(n) for the dp array
        dp = [False]*(len(s) + 1)
        dp[0] = True # For empty string
        for index in range(1,len(s)+1):
            for word in wordDict:
                if dp[index - len(word)] and s[:index].endswith(word):
                    dp[index] = True
        return dp[-1]
