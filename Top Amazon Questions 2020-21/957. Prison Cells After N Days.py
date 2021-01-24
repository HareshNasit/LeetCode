def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Runtime: O(K*min(N,2^K) where K = number of cells 8 here
        # Space: O(K*2^K)
        hasCycle = False
        days = 0
        states = dict()
        for i in range(N):
            next_d = self.next_day(cells)
            if tuple(next_d) not in states:
                states[tuple(next_d)] = 1
                days += 1
            else:
                hasCycle = True
                break
            cells = next_d
        if hasCycle:
            index = N % days
            while index > 0:
                cells = self.next_day(cells)
                index -= 1
            return cells
        return cells

    def next_day(self, cells):
        # print(cells)
        temp_cells = cells[:]
        for i in range(8):
            if i == 0 or i == 7:
                temp_cells[i] = 0
                continue
            if cells[i-1] == cells[i+1]:
                temp_cells[i] = 1
            else:
                temp_cells[i] = 0
        return temp_cells
        # Brute Force
        # Runtime: O(N^2)
        # Space: O(2N)
        # temp_prison = cells[:]
        # for day in range(N):
        #     fixed_temp_prison = temp_prison[:]
        #     for i in range(1,8-1):
        #         if fixed_temp_prison[i-1] == fixed_temp_prison[i+1]:
        #             temp_prison[i] = 1
        #         else:
        #             temp_prison[i] = 0
        #     temp_prison[-1] = 0
        #     # print(temp_prison)
        # return temp_prison
