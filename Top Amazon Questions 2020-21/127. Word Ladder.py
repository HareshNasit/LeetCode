def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Use words as nodes and the transformation as an edge.BytesWarning
        # Graph to store the word dictionary of possible words after transformation
        # sequence.
        # Perform a Breadth First Search to find the shortest path between the 2 nodes.
        # Runtime: O(M^2*N)
        # Space: O(M^2*N), each word will have M combinations and the original word
        # Each word requires M^2 space and there are N such words.
        if endWord not in wordList:
            return 0
        graph = defaultdict(list)

        # Create the graph from the words in dict.
        # O(M^2*N)
        for word in wordList:
            for i in range(len(word)):
                # E.g. *ot, h*t, l*t, lo*, etc..
                graph[word[:i] + "*" + word[i+1:]].append(word)

        queue = []
        queue.append((beginWord,1)) # (word, level)
        visited = {beginWord: True}
        # O(M^2*N)
        while queue:
            curr_word, level = queue.pop(0)
            for i in range(len(curr_word)):
                # Go through all the possible transformations to get the shortest path.
                intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]
                neighbours = graph[intermediate_word]

                for next_word in neighbours:
                    if next_word == endWord:
                        return level + 1
                    if next_word not in visited:
                        visited[next_word] = True
                        queue.append((next_word,level+1))
                graph[intermediate_word] = [] # To Speed up and not visit the words again
        return 0
