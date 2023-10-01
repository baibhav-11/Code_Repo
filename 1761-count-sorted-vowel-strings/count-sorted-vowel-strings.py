class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Initialize a 2D array dp[i][j] to store count of valid strings of length i ending with vowel j.
        dp = [[0] * 5 for _ in range(n + 1)]
        
        # Initialize the base case: there's one valid string of length 1 for each vowel.
        for j in range(5):
            dp[1][j] = 1
        
        # Fill in the dp array using dynamic programming.
        for i in range(2, n + 1):
            for j in range(5):
                # dp[i][j] is the sum of dp[i-1][k] where k >= j (since it's lexicographically sorted).
                dp[i][j] = sum(dp[i-1][k] for k in range(j, 5))
        
        # Sum up all the valid strings of length n.
        return sum(dp[n])
