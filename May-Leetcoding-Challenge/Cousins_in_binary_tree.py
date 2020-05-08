# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_info = self.get_depth(root,x,0,root)
        y_info = self.get_depth(root,y,0,root)
        same_depth = x_info[0] == y_info[0]
        diff_parent = x_info[1] != y_info[1]
        return same_depth and diff_parent

    def get_depth(self, root, value, depth,parent):

        if root == None:
            return []
        if root.val == value:
            return [depth,parent.val]
        return self.get_depth(root.left,value,depth+1, root) + self.get_depth(root.right,value,depth+1, root)
