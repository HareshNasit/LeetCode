def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Runtime: O(N)
        # Space: O(1)

        longest_time = 0
        longest_key = ""
        for i in range(len(keysPressed)):
            if i == 0:
                longest_time = releaseTimes[i]
                longest_key = keysPressed[i]
                continue
            if releaseTimes[i] - releaseTimes[i-1] > longest_time:
                longest_time = releaseTimes[i] - releaseTimes[i-1]
                longest_key = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i-1] == longest_time:
                if ord(keysPressed[i]) > ord(longest_key):
                    longest_key = keysPressed[i]
        return longest_key
