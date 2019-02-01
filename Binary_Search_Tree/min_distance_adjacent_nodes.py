def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_diff = 0
        right_diff = 0
        if root.left != None:
            left_diff = root.val - root.left.val
            left_diff = self.min_value(left_diff, self.minDiffInBST(root.left))
        if root.right != None:
            right_diff = root.right.val - root.val
            right_diff = self.min_value(right_diff, self.minDiffInBST(root.right))
        return self.min_value(left_diff, right_diff)
    
    def min_value(self,left_diff, right_diff):
        if left_diff != 0  and right_diff ==0:
            return left_diff
        elif right_diff != 0 and left_diff == 0:
            return right_diff
        return min(left_diff,right_diff)
