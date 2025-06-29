from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define pointers
        left = 0
        right = 1

        # define maxProfit and currentPrice
        maxProfit = 0
        
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right

            right += 1

        return maxProfit
    
S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))
print(S.maxProfit([1,2,4]))