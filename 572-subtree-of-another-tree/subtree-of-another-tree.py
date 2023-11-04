# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Check if the tree rooted at "node" is identical to the tree rooted at "subRoot"
        def isIdentical(node, subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            return (node.val == subRoot.val) and isIdentical(node.left, subRoot.left) and isIdentical(node.right, subRoot.right)
        
        # Check if the tree rooted at "root" contains a subtree that is identical to "subRoot"
        def containsSubtree(root, subRoot):
            if not root:
                return False
            if isIdentical(root, subRoot):
                return True
            return containsSubtree(root.left, subRoot) or containsSubtree(root.right, subRoot)
        
        return containsSubtree(root, subRoot)