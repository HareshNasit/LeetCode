class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Logic is to find the equation of the line and check
        # if all the points satisfy the equation.
        if len(coordinates) == 2:
            return True
        dx = coordinates[0][0] - coordinates[1][0]
        dy = coordinates[0][1] - coordinates[1][1]
        xp =  dx*coordinates[0][1] - dy*coordinates[0][0]
        for i in range(2,len(coordinates)):
            if dx*coordinates[i][1] - dy*coordinates[i][0] != xp:
                return False
        return True
