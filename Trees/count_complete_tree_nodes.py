def countNodes(self, root):
        """
        https://leetcode.com/problems/count-complete-tree-nodes/
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
