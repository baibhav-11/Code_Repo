from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        count = 0  # Total count of arithmetic subsequences
        
        # dp[i] is a dictionary that stores the count of arithmetic subsequences ending at index i with a specific difference
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                # Calculate the difference between nums[i] and nums[j]
                diff = nums[i] - nums[j]
                
                # Update the count of subsequences with the current difference
                dp[i][diff] += 1
                
                # If there is a previous index k such that nums[j] - nums[k] == diff,
                # then add the count of subsequences ending at index k with difference diff to the count of subsequences ending at index i
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    count += dp[j][diff]
        
        return count