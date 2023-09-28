class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Pad the shorter string with leading zeros to make their lengths equal.
        len_a, len_b = len(a), len(b)
        max_len = max(len_a, len_b)
        a = '0' * (max_len - len_a) + a
        b = '0' * (max_len - len_b) + b

        # Perform binary addition from right to left.
        for i in range(max_len - 1, -1, -1):
            bit_a, bit_b = int(a[i]), int(b[i])
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        # If there's a carry left after adding all bits, append it to the result.
        if carry:
            result.append(str(carry))

        # Reverse the result and join it to form the binary string.
        return ''.join(result[::-1])
