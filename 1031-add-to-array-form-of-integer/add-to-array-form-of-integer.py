class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        
        # Iterate over the digits in the 'num' array and the 'k' integer from right to left.
        i = len(num) - 1
        while i >= 0 or k > 0 or carry:
            # Get the rightmost digit from 'num' and 'k'.
            digit_num = num[i] if i >= 0 else 0
            digit_k = k % 10 if k > 0 else 0
            k //= 10
            
            # Calculate the sum and carry.
            total = digit_num + digit_k + carry
            result.append(total % 10)
            carry = total // 10
            
            i -= 1
        
        # Continue processing carry until it becomes zero.
        while carry:
            result.append(carry % 10)
            carry //= 10
        
        # Reverse the result to get the correct order.
        return result[::-1]