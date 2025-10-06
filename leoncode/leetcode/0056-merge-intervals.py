# 56 - https://leetcode.com/problems/merge-intervals/

# Time: O(N log N) - sorting the intervals
# Space: O(N) - for the result list
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = res[-1]

            if start > prevEnd:
                res.append([start, end])
            else:
                res[-1] = [
                    min(start, prevStart),
                    max(end, prevEnd)
                ]

        return res
