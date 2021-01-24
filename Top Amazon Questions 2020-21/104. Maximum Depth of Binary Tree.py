def maxDepth(self, root: TreeNode) -> int:
        # Runtime: O(N) traversing all the nodes
        # Space: O(N) recursion
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
