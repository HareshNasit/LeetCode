def searchInsert(self, nums, target):
        """
        https://leetcode.com/problems/search-insert-position/
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Runs in O(logn)
        start = 0
        end = len(nums)
        while start < end:
            mid = start+(end-start)//2
            print(mid)
            print("start " + str(start))
            print("End " + str(end))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid
        return start
        #OR a Cheeky way but runs in O(nlogn)
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)
