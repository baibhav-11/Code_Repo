class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        
        # Calculate XOR of ASCII values of characters in string s
        for char in s:
            result ^= ord(char)
        
        # XOR the result with ASCII values of characters in string t
        for char in t:
            result ^= ord(char)
        
        # Convert the final result back to a character
        return chr(result)
