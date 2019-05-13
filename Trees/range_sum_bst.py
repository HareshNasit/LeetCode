def rangeSumBST(self, root, L, R):
        """
        https://leetcode.com/problems/range-sum-of-bst/submissions/
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        if root:
            if L <= root.val <= R:
                total += root.val
            if L < root.val:
                total += self.rangeSumBST(root.left,L,R)
            if root.val < R:
                total += self.rangeSumBST(root.right,L,R)
        return total
