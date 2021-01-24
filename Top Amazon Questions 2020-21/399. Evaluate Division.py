# Runtime: O(M*N) where M is the num. of queries, N is the num. of nodes
        # Space: O(N) where N is the num. of nodes not considering the result array.
        def dfs(graph,curr_n, target_n, cum_prod, visited):
            visited.add(curr_n)
            neighbours = graph[curr_n]

            return_prod = -1
            if target_n in neighbours:
                return_prod = cum_prod*neighbours[target_n]
            else:
                for neighbour, value in neighbours.items():
                    if neighbour in visited:
                        continue
                    return_prod = dfs(graph,neighbour,target_n,cum_prod*value,visited)
                    # Once it finds a result, we can break
                    if return_prod != -1:
                        break
            # visited.remove(curr_n)
            return return_prod


        # Step1: Build the graph from the given equations
        # Node denotes the variable and the edge is the result of divison.
        graph = defaultdict(defaultdict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]

        # Step2: Handle the 2 edge cases and call dfs on the given queries.
        result_list = []
        for query in queries:
            # Note: Order of the if loops matter. E.g. if input query = x and x
            # but x does not exist in graph, we cannot return 1 and should return -1
            # If either 1 of the input nodes is not in the graph, return -1
            if query[0] not in graph or query[1] not in graph:
                result_list.append(-1)
            # If the 2 input nodes are the same. E.g. a/a
            elif query[0] == query[1]:
                result_list.append(1)
            # Run DFS on the 2 valid input nodes.
            else:
                visited = set()
                result_list.append(dfs(graph,query[0], query[1], 1,visited))

        return result_list
