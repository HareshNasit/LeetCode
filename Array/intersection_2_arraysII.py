def intersect(self, nums1, nums2):
        """
        https://leetcode.com/problems/intersection-of-two-arrays-ii/
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        intersection = []
        for i in nums1:
            if i not in nums1_dict:
                nums1_dict[i] = 1
            else:
                nums1_dict[i] += 1
        for j in nums2:
            if j in nums1_dict and nums1_dict[j] > 0:
                intersection.append(j)
                nums1_dict[j] -= 1
        return intersection
