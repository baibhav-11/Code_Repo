# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countSubtreeAverages(self, root, count):
        if not root:
            return (0, 0)  # Sum and Count
        
        left_sum, left_count = self.countSubtreeAverages(root.left, count)
        right_sum, right_count = self.countSubtreeAverages(root.right, count)
        
        # Calculate the sum and count for the current subtree
        subtree_sum = left_sum + right_sum + root.val
        subtree_count = left_count + right_count + 1
        
        subtree_average = subtree_sum / subtree_count
        
        if root.val == int(subtree_average):
            count[0] += 1  # Increment the count if the value matches the average
        
        return (subtree_sum, subtree_count)
    
    def averageOfSubtree(self, root):
        count = [0]  # Initialize count as a list to allow for mutable reference
        self.countSubtreeAverages(root, count)
        return count[0]
