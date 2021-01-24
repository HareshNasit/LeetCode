#Runtime: O(m+n) = O(n)
    # Space: O(n)
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root is None or target is None:
            return []

        graph = defaultdict(set)
        self.build_graph(graph, root, None)
        return self.bfs(graph, target, K)

    def build_graph(self,graph, root, parent):
        if root and parent:
            graph[root].add(parent)
            graph[parent].add(root)

        if root.left:
            self.build_graph(graph, root.left, root)
        if root.right:
            self.build_graph(graph, root.right, root)

    def bfs(self, graph, target, K):
        visited = {target: 1}
        queue = [(target, 0)]
        k_dst_away = []
        while queue:
            node, num_nodes = queue.pop(0)
            if num_nodes == K:
                k_dst_away.append(node.val)
            for neigh_node in graph[node]:
                if neigh_node not in visited:
                    queue.append((neigh_node, num_nodes+1))
                    visited[neigh_node] = 1
        return k_dst_away
            
