# 746 - https://leetcode.com/problems/min-cost-climbing-stairs/

# Time: O(n)
# Space: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        one, two = cost[-2], cost[-1]
        
        for i in range(len(cost) - 3, -1, -1):
            temp = one
            one = min(cost[i] + one, cost[i] + two)
            two = temp

        return min(one, two)