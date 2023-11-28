# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # (node, position)
        
        while queue:
            level_size = len(queue)
            _, leftmost_pos = queue[0]
            
            for i in range(level_size):
                node, pos = queue.popleft()
                relative_pos = pos - leftmost_pos
                
                if node.left:
                    queue.append((node.left, 2 * relative_pos))
                if node.right:
                    queue.append((node.right, 2 * relative_pos + 1))
                
            max_width = max(max_width, relative_pos + 1)
        
        return max_width