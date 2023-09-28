class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit.
        n = len(digits)
        carry = 1  # Initialize the carry to 1 to add one.
        
        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10  # Update the current digit.
            carry = total // 10  # Calculate the carry for the next digit.
        
        # If there's still a carry, add it as a new digit to the left.
        if carry:
            digits.insert(0, carry)
        
        return digits
