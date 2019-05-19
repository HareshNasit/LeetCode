def preorder(self, root):
        """
        https://leetcode.com/problems/n-ary-tree-preorder-traversal/
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val] 
        for child in root.children:    
            result.extend(self.preorder(child))     
        return result
