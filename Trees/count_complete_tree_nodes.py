def countNodes(self, root):
        """
        https://leetcode.com/problems/count-complete-tree-nodes/
        :type root: TreeNode
        :rtype: int
        """
        #O(n)
        #if root is None:
            #return 0
        #return self.countNodes(root.left) + self.countNodes(root.right) + 1
        #O((log(n)^2)
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_tree = root.left
        left_height = 0
        while left_tree:
            left_height += 1
            left_tree = left_tree.left
        right_tree = root.right
        right_height = 0
        while right_tree:
            right_height += 1
            right_tree = right_tree.left
        print left_height
        print right_height
        if left_height == right_height:
            return  2**left_height + self.countNodes(root.right)
        else:
            return  2**right_height  + self.countNodes(root.left)
