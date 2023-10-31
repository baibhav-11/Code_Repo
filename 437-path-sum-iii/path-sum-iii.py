# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, summ: int) -> int:
    if not root:
      return 0

    def dfs(root: TreeNode, summ: int) -> int:
      if not root:
        return 0
      return (summ == root.val) + \
          dfs(root.left, summ - root.val) + \
          dfs(root.right, summ - root.val)

    return dfs(root, summ) + \
        self.pathSum(root.left, summ) + \
        self.pathSum(root.right, summ)
