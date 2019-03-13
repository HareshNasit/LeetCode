def isSymmetric(self, root):
        """
        https://leetcode.com/problems/symmetric-tree/
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.same_nodes(root.left,root.right)
def same_nodes(self, left, right):
    if left == None and  right == None:
        return True
    if left == None or right == None:
        return False
    if left.val == right.val:
        return self.same_nodes(left.left, right.right) and                                       self.same_nodes(left.right, right.left)
    return False

    
