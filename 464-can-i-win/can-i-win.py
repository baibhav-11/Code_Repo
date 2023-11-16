class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False  # It's impossible to win

        memo = {}

        def canWin(mask, remaining):
            if remaining <= 0:
                return False  # The opponent already reached or exceeded the desiredTotal

            if mask in memo:
                return memo[mask]

            for i in range(maxChoosableInteger):
                bit = 1 << i
                if (mask & bit) == 0:  # If the number is not chosen yet
                    new_mask = mask | bit
                    if not canWin(new_mask, remaining - (i + 1)):
                        memo[mask] = True
                        return True

            memo[mask] = False
            return False

        return canWin(0, desiredTotal)