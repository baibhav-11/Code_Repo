class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        prefix = [0] * n
        
        # Build the prefix array using the KMP algorithm.
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]
            
            if s[i] == s[j]:
                j += 1
            prefix[i] = j
        
        # Check if the last value in the prefix array divides n.
        return prefix[-1] > 0 and n % (n - prefix[-1]) == 0

        