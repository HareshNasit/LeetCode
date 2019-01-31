def intersection(self, nums1, nums2):
        """
        https://leetcode.com/problems/intersection-of-two-arrays/submissions/
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        output_list = []
        for i in nums1_set:
            if i in nums2_set:
                output_list.append(i)
        return output_list
