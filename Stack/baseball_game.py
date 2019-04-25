def calPoints(self, ops):
        """
        https://leetcode.com/problems/baseball-game/
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for i in ops:
            if i == '+':
                scores.append(scores[-1] + scores[-2])
            elif i == 'D':
                scores.append(2*scores[-1])
            elif i == 'C':
                scores.pop()
            else:
                scores.append(int(i))
        return sum(scores)
