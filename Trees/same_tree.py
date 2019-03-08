def isSameTree(self, p, q):
        """
        https://leetcode.com/problems/same-tree/
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and
            self.isSameTree(p.right,q.right)
