class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_length = -1
        char_index = {}  # Dictionary to store the most recent index of each character
        
        for i, char in enumerate(s):
            if char in char_index:
                max_length = max(max_length, i - char_index[char] - 1)
            else:
                char_index[char] = i

        return max_length
