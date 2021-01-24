def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Breadth first search using while loop
        # Runtime: O(n^2)
        # Space: O(n^2)

        islands_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Perform a Breadth First Search
                    queue = [(i,j)]
                    path = "X"
                    grid[i][j] = 0

                    while queue:
                        x,y = queue.pop(0)
                        if (x > 0 and grid[x-1][y] == 1):
                            queue.append((x-1,y))
                            grid[x-1][y] = 0
                            path += "U"
                        else:
                            path += "O"

                        if (y > 0 and grid[x][y-1] == 1):
                            queue.append((x,y - 1))
                            grid[x][y-1] = 0
                            path += "L"
                        else:
                            path += "O"

                        if (x < len(grid) - 1 and grid[x+1][y] == 1):
                            queue.append((x+1,y))
                            grid[x+1][y] = 0
                            path += "D"
                        else:
                            path += "O"

                        if (y < len(grid[0]) - 1  and grid[x][y+1] == 1):
                            queue.append((x,y+1))
                            grid[x][y+1] = 0
                            path += "R"
                        else:
                            path += "O"
                    islands_set.add(path)
        return len(islands_set)





        # Using Depth First Search and a set
        # Runtime: O(n^2)
        # Space: O(n^2)
#         islands_set = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     path = self.dfs(grid,i,j,len(grid),len(grid[0]),"X")
#                     islands_set.add(path)
#         return len(islands_set)

#     def dfs(self,grid,i,j,m,n,sym):
#         if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
#             return "0"
#         grid[i][j] = 0
#         up = self.dfs(grid,i-1,j,m,n,"U")
#         right = self.dfs(grid,i,j+1,m,n,"R")
#         down = self.dfs(grid,i+1,j,m,n,"D")
#         left = self.dfs(grid,i,j-1,m,n,"L")
#         return sym + up + right + down + left
