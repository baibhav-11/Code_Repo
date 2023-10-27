class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Calculate the XOR of x and y
        xor_result = x ^ y
        
        # Count the set bits (1s) in the XOR result
        hamming_distance = 0
        while xor_result:
            hamming_distance += xor_result & 1
            xor_result >>= 1

        return hamming_distance
