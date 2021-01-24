def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Runtime: O(n) Since we traverse all the elements
        # Space: O(n) Space for keeping track of a stack
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break # Because the remaining stack remains the same
            else:
                stack.append(asteroid)
        return stack
