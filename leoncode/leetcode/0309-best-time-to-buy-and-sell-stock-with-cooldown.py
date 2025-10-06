# 309 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using cache, key (i, isBuying) and value is max_profit
        dp = {}

        def dfs(i, isBuying):
            # constraint
            if i >= len(prices):
                return 0
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]

            if isBuying:
                buy = dfs(i + 1, not isBuying) - prices[i]
                cooldown = dfs(i + 1, isBuying)
                dp[(i, isBuying)] = max(buy, cooldown)
            else:
                # `i + 2` because after we sell, we can't perform buy or sell, 
                # only can perform cooldown
                sell = dfs(i + 2, not isBuying) + prices[i]
                cooldown = dfs(i + 1, isBuying)
                dp[(i, isBuying)] = max(sell, cooldown)

            return dp[(i, isBuying)]

        return dfs(0, True)