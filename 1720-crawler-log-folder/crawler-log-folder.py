class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # Represents the depth in the folder structure
        for log in logs:
            if log == "./":
                continue  # Remain in the same folder
            elif log == "../":
                if depth > 0:
                    depth -= 1  # Move up one level in the folder structure
            else:
                depth += 1  # Move down to a child folder

        return depth