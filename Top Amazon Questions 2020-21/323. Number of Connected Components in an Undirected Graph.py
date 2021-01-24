def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Depth First Search
        # Runtime: O(n^2)
        # Space: O(n^2)
        # Space and Time can be improved by using a dict instead of
        # matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(edges)):
            edge = edges[i]
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
        # Depth First Search
        count = 0
        visited = [False]*(n)
        for i in range(n):
            if not visited[i]:
                visited = self.dfs(matrix,i,visited,n)
                count += 1
        return count

    def dfs(self,matrix,i,visited,n):
        visited[i] = True
        for j in range(n):
            if matrix[i][j] == 1 and (not visited[j]):
                visited = self.dfs(matrix,j,visited,n)
        return visited
