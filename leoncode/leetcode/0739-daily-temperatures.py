# 739 - https://leetcode.com/problems/daily-temperatures/

# Time: O(n)
# Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores cooler temperatures
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and temp > stack[-1][0]:
                coolerTemp, prevDay = stack.pop()
                days = i - prevDay
                res[prevDay] = days

            stack.append((temp, i))
        
        return res
