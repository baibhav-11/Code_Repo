class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case
        if n == 1:
            return 0

        # Calculate the mid point of the (n-1)th row
        mid = 2**(n-2)

        # If k is in the first half of the (n-1)th row
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            # If k is in the second half, find the complement in the (n-1)th row
            return 1 - self.kthGrammar(n-1, k - mid)
