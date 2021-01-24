def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 2 pointers problem
        # nums1[:] = sorted(nums1[:m] + nums2) # Runtime O((m+n)*log(m+n)) Brute Force
        #  Runtime: O(m+n), Space: O(m)
        # ptr1 = 0
        # ptr2 = 0
        # nums1_copy = nums1[:m] # O(m)
        # nums1[:] = []
        # while ptr1 < m and ptr2 < n:
        #     if nums1_copy[ptr1] < nums2[ptr2]:
        #         nums1.append(nums1_copy[ptr1])
        #         ptr1 += 1
        #     else:
        #         nums1.append(nums2[ptr2])
        #         ptr2 += 1
        #
        # if ptr1 < m:
        #     nums1[ptr1 + ptr2:] = nums1_copy[ptr1:]
        # if ptr2 < n:
        #     nums1[ptr1 + ptr2:] = nums2[ptr2:]

        # 2 pointers modifying nums1 directly and saving space
        # Runtime: O(m+n), Space: O(1)
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 has elements p1 = 0, concat remaining elements to nums1 start.
        # If nums1 has elements and p2 = 0, its sorted by default.
        nums1[:p2 + 1] = nums2[:p2 + 1]

        # ptr1 = 0
        # ptr2 = 0
        # if len(nums2) == 0:
        #     return nums1
        # while ptr1 + ptr2 < m + 2*n:
        #     if ptr1 < m and nums1[ptr1] <= nums2[ptr2]:
        #         ptr1 += 1
        #     elif ptr2 < n:
        #         if ptr1 < m and nums2[ptr2] < nums1[ptr1]:
        #             nums1[ptr1], nums2[ptr2] = nums2[ptr2], nums1[ptr1]
        #             ptr1 += 1
        #         else:
        #             nums1[ptr1] = nums2[ptr2]
        #             ptr1 += 1
        #             ptr2 += 1
