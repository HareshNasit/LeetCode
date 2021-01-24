def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Brute force is 2 for loops and creating a longest overlap for each
        # interval. Time: O(n^2)
        # Approach 2: Sorting, Runtime: O(nlogn), Space Complexity: O(n) because creation of new list
        intervals.sort(key=lambda x: x[0]) # Sorting take nlogn time
        print(intervals)
        merged_intervals = []
        # Traversal takes O(n) time
        for interval in intervals:
            if len(merged_intervals) == 0:
                merged_intervals.append(interval)
                continue
            if interval[0] <= merged_intervals[-1][1]:
                last_interval = merged_intervals[-1]
                merged_intervals[-1] = [last_interval[0], max(interval[1], last_interval[1])]
            else:
                merged_intervals.append(interval)
        return merged_intervals
