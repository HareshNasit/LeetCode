def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Runtime: O(N) Calling DFS only once for all the elements traversal
        # Space: O(N)
        def dfs(discovery_time, prev_v, curr_v):
            visited.add(curr_v)
            lowest_rank[curr_v] = discovery_time
            for next_v in graph[curr_v]:
                if next_v != prev_v:
                    if next_v not in visited:
                        dfs(discovery_time+1,curr_v,next_v)

                    lowest_rank[curr_v] = min(lowest_rank[next_v], lowest_rank[curr_v])
                    if lowest_rank[next_v] > discovery_time:
                        critical_connections.append([curr_v, next_v])



        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        critical_connections = []
        lowest_rank = [-1 for _ in range(n)]
        discovery_time = 0
        prev_vertex = -1
        curr_vertex = 0
        dfs(discovery_time, prev_vertex, curr_vertex)
        return critical_connections
