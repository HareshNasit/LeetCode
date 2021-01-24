def partitionLabels(self, S: str) -> List[int]:
        # Greedy Algorithm to get the last index of all the letters
        # and keep track of the start and the max index of
        # the smallest partition.
        # Runtime: O(n), Space: O(1) since 26 letters dict(constant)
        last_index = {}
        # Get the last index of all the letters
        for i, s in enumerate(S):
            last_index[s] = i
        output_lst = []
        start = 0
        streak = 0
        for i, s in enumerate(S):
            streak = max(last_index[s], streak)
            if (i == streak):
                output_lst.append(streak - start + 1)
                start = i + 1
        return output_lst

        # # Runtime: O(n^2), Space: O(1) since there are only 26 letters(constant)
        # freqs = {}
        # # O(n) for string traversal
        # for i in S:
        #     if i not in freqs:
        #         freqs[i] = 1
        #     else:
        #         freqs[i] += 1
        # temp_freqs = {}
        # partition_ints = []
        # # O(n) for string traversal
        # for letter in S:
        #     if letter not in temp_freqs:
        #         temp_freqs[letter] = 1
        #     else:
        #         temp_freqs[letter] += 1
        #     is_partition = True
        #     count = 0
        #     # O(n) for string traversal again
        #     for j in temp_freqs:
        #         is_partition = is_partition and (freqs[j] == temp_freqs[j])
        #         if is_partition is False:
        #             break
        #         count += temp_freqs[j]
        #     if is_partition is True:
        #         partition_ints.append(count)
        #         temp_freqs = {}
        # return partition_ints
