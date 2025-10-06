# 322 - https://leetcode.com/problems/coin-change/

# Time: O(amount × len(coins))
# Space: O(n) where n is amount

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming Solution
        # index is amount and value is number of coins
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # base case

        # for each amount, we want to find the minimum number of coins to reach that amount (if possible)
        for am in range(amount+1):
            for coin in coins:
                diff = am - coin
                if diff >= 0:
                    # attempt to find a matching diff amount `dp[diff] --> min number of coins`
                    dp[am] = min(dp[am], 1 + dp[diff])

        return dp[amount] if dp[amount] != float('inf') else -1