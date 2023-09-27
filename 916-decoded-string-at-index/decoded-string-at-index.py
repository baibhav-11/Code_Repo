class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0

        # Calculate the length of the decoded string without actually storing it.
        for c in s:
            if c.isdigit():
                repeat = int(c)
                decoded_length *= repeat
            else:
                decoded_length += 1

        # Iterate through the encoded string in reverse to find the character at index k.
        for c in reversed(s):
            if c.isdigit():
                repeat = int(c)
                decoded_length //= repeat
                k %= decoded_length
            elif k % decoded_length == 0:
                return c
            else:
                decoded_length -= 1

        return s[0]  # In case k exceeds the length of the decoded string.