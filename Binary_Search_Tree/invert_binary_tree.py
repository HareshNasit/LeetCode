def invertTree(self, root):
        """
        https://leetcode.com/problems/invert-binary-tree/
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root
