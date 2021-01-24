def findCircleNum(self, isConnected: List[List[int]]) -> int:
                # Depth First Search to find all the connected components
        # Runtime: O(n^2) for traversal of all the nxn elements of isConnected
        # Space: O(n) for tracking the visited array
        visited = [False]* len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                # Every time we this if loop executes, a new province
                # is counted for.
                visited = self.dfs(isConnected,i,visited)
                count += 1
        return count

    def dfs(self,isConnected, i,visited):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] and (not visited[j]):
                visited = self.dfs(isConnected,j,visited)
        return visited

    # Breadth First Search Approach
    # Runtime: O(n^2)
    # Space: O(n)
    # visited = [False] * len(isConnected)
    # count = 0
    # for i in range(len(isConnected)):
    #     if not visited[i]:
    #         queue = [i]
    #         while queue:
    #             x = queue.pop(0)
    #             for j in range(len(isConnected)):
    #                 if isConnected[x][j] and (not visited[j]):
    #                     queue.append(j)
    #             visited[x] = True
    #         count += 1
    # return count
