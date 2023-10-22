# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize a variable to store the maximum path sum
        self.max_sum = float('-inf')

        # Define a recursive function to calculate the maximum path sum
        def max_path_sum(node):
            if not node:
                return 0

            # Calculate the maximum path sum in the left and right subtrees
            left_sum = max(max_path_sum(node.left), 0)
            right_sum = max(max_path_sum(node.right), 0)

            # Calculate the maximum path sum that includes the current node
            current_sum = node.val + left_sum + right_sum

            # Update the maximum path sum if the current sum is greater
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum path sum that can be extended from the current node
            return node.val + max(left_sum, right_sum)

        # Start the recursion from the root node
        max_path_sum(root)

        return self.max_sum 