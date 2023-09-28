class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n,m = len(a), len(b)
        max_repeats = (m + n - 1) // n

        for i in range(2):
            repeated = a * (max_repeats + i)
            if b in repeated:
                return max_repeats + i 
        return -1 