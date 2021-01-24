def connectSticks(self, sticks: List[int]) -> int:
        # Greedy Problem
        # Runtime: O(N) + O(3N*logN)
        # Space: O(1) since we use the given sticks as heap
        heapq.heapify(sticks)
        cost = 0
        print(sticks)
        # O(N*3*logN)
        while len(sticks) > 1:
            a = heapq.heappop(sticks) # O(logN)
            b = heapq.heappop(sticks) # O(logN)
            heapq.heappush(sticks,a+b) # O(logN)
            cost += a + b
        return cost
        # Brute Force: Greedily always select 2 sticks with the lowest
        # lengths and append the sum and resort the list of sticks
        # Runtime: O(N^2*logn)
        # Space: O(1)
        # sticks.sort(reverse=True)
        # cost = 0
        # while len(sticks) > 1:
        #     elem1 = sticks.pop()
        #     elem2 = sticks.pop()
        #     cost += elem1 + elem2
        #     sticks.append(elem1 + elem2)
        #     sticks.sort(reverse=True)
        # return cost
