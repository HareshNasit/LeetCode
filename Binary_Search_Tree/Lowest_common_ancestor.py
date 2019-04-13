def lowestCommonAncestor(self, root, p, q):
        """
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print(root.val)
        if ((p.val < root.val and q.val > root.val)):
            print("hello")
            return root
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
