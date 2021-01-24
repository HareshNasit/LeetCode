def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Runtime: O(N)
        # Space: O(N)
        time_modulos = defaultdict(int)
        count = 0
        for t in time:
            if (t%60 == 0):
                count += time_modulos[t%60]
            count += time_modulos[60 - (t%60)]
            time_modulos[t%60] += 1
        return count
        # Brute Force
        # Runtime: O(N^2)
        # Space: O(1)
        # count = 0
        # for i in range(len(time)):
        #     for j in range(i+1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             # print(time[i], time[j])
        #             count += 1
        # return count
