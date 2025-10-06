# 134 - https://leetcode.com/problems/gas-station/

# Time: O(n)
# Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost): return -1

        sumGas, sumCost = 0, 0
        startingIndex = 0
        leftoverGas = 0
        numStations = len(gas)

        for i in range(numStations):
            sumGas += gas[i]
            sumCost += cost[i]

            leftoverGas += gas[i] - cost[i]
            if leftoverGas < 0:
                startingIndex = i + 1
                leftoverGas = 0 # greedy, reset to 0

        return startingIndex if sumGas >= sumCost else -1
