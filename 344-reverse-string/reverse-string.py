class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right= 0, len(s) -1 
        while left < right:  # Continue swapping until the pointers meet or cross
            s[left], s[right] = s[right], s[left]  # Swap the characters at the two pointers
            left += 1  # Move the left pointer one step to the right
            right -= 1  # Move the right pointer one step to the left