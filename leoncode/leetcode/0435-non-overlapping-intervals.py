# 435 - https://leetcode.com/problems/non-overlapping-intervals/

# Time: O(n log n)
# Space: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prevEnd:
                prevEnd = end
            else:
                # overlap found, pick a "smaller" end so we are less likely to overlap
                # in subsequent intervals
                res += 1
                prevEnd = min(prevEnd, end)

        return res
