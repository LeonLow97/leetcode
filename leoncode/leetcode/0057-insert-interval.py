# 57 - https://leetcode.com/problems/insert-interval/

# Time: O(N)
# Space: O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            intStart, intEnd = newInterval

            if intStart > end:
                res.append([start, end])
            elif intEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # overlap
                newInterval = [
                    min(start, intStart),
                    max(end, intEnd)
                ]

        res.append(newInterval)
        return res
