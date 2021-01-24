def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Runtime: O(nlogn), Space: O(1)
        intervals.sort(key=lambda x: x[0]) # O(nlogn)
        # O(n)
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
