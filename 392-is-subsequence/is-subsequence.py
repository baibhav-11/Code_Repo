class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        s_pointer, t_pointer = 0, 0
        
        # Iterate through the characters of both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If the characters match, move the s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Move the t_pointer in any case
            t_pointer += 1
        
        # Check if we've iterated through the entire s string
        return s_pointer == len(s)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    result1 = solution.isSubsequence("abc", "ahbgdc")
    print(result1)  # Output: True
    
    result2 = solution.isSubsequence("axc", "ahbgdc")
    print(result2)  # Output: False
