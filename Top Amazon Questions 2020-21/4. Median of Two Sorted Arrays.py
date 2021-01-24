def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time: O(m + n), Space: O(m+n)
        # Logic: Merge the 2 lists into 1 sorted list and find the median.
        merged_lst = []
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] <= nums2[ptr2]:
                merged_lst.append(nums1[ptr1])
                ptr1 += 1
            else:
                merged_lst.append(nums2[ptr2])
                ptr2 += 1
        if ptr1 < len(nums1):
            merged_lst += nums1[ptr1:]
        if ptr2 < len(nums2):
            merged_lst += nums2[ptr2:]

        index = len(merged_lst) // 2
        if (len(merged_lst) % 2 == 0):
            median = (merged_lst[index] + merged_lst[index - 1]) / 2.0
            return median
        else:
            return merged_lst[index]
