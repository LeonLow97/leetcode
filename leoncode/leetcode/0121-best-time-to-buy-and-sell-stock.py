# 121 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Optimal: Sliding Window / Two Pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0

        for right, price in enumerate(prices):
            if price <= prices[left]:
                left = right
            else:
                res = max(res, price - prices[left])
        
        return res
