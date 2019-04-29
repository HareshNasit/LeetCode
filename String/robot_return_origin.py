def judgeCircle(self, moves):
        """
        https://leetcode.com/problems/robot-return-to-origin/
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
            else:
                return False
        return x == 0 and y == 0
