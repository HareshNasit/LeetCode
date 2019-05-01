def findDuplicate(self, nums):
        """
        https://leetcode.com/problems/find-the-duplicate-number/
        :type nums: List[int]
        :rtype: int
        """
        #Runtime is O(n)
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
            if nums_dict[i] == 2:
                return i
        return 0

        #OR USE A SET TO CHECK IF A GIVEN ELEMENT IS IN IT. RUNTIME IS O(n).
