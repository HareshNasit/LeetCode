def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(n) Worst case the grid is filled with rotten oranges
        mins = -1
        queue = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        queue.append((-1,-1))
        while queue:
            print(queue)
            x,y = queue.pop(0)
            if x == -1:
                mins += 1
                if queue:
                    queue.append((-1,-1))
            else:
                #Up
                if (x > 0 and grid[x-1][y] == 1):
                    grid[x-1][y] = 2
                    queue.append((x-1,y))
                    fresh -= 1

                 #Right
                if (y <  len(grid[i]) -1 and grid[x][y+1] == 1):
                    grid[x][y+1] = 2
                    queue.append((x,y+1))
                    fresh -= 1

                 #Down
                if (x < len(grid) - 1  and grid[x+1][y] == 1):
                    grid[x+1][y] = 2
                    queue.append((x+1,y))
                    fresh -= 1

                 #Left
                if (y > 0 and grid[x][y-1] == 1):
                    grid[x][y-1] = 2
                    queue.append((x,y-1))
                    fresh -= 1
        return mins if fresh == 0 else -1
