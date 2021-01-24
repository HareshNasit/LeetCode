def trap(self, height: List[int]) -> int:
        # Runtime: O(n) Using Dynamic Programming
        # Space: O(2n)
        left_max = []
        right_max = []
        for i in range(len(height)):
            if i == 0:
                left_max.append(height[i])
                continue
            left_max.append(max(left_max[i-1], height[i]))
        for j in range(len(height) - 1, -1, -1):
            if j == len(height) - 1:
                right_max.append(height[j])
                continue
            right_max.append(max(right_max[-1], height[j]))
        right_max.reverse()
        water = 0
        for k in range(len(height)):
            valid = min(left_max[k], right_max[k]) - height[k]
            if valid > 0:
                water += valid
        return water



        # Brute Force
        # Runtime: O(n^2)
        # Space: O(1)
        # water = 0
        # for i in range(len(height)):
        #     left_max = 0
        #     right_max = 0
        #     for j in range(0,i):
        #         left_max = max(left_max, height[j])
        #     for k in range(i+1,len(height)):
        #         right_max = max(right_max, height[k])
        #     if min(left_max,right_max) - height[i] > 0:
        #         water += (min(left_max,right_max) - height[i])
        # return water
