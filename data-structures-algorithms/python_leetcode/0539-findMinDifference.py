'''
Difficulty: MEDIUM
No.539    https://leetcode.com/problems/minimum-time-difference/

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum 
minutes difference between any two time-points in the list.
'''

from typing import List

# Eric's Solution
# Runtime: 65 ms, Memory: 16.9 MB
# Time complexity: O(n log n), Space complexity: O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertToMinutes(time):
            timeArr = time.split(":")
            timeMin = int(timeArr[0]) * 60 + int(timeArr[1])
            return timeMin

        # Extracting the number of minutes
        maxMinutes = 0
        setMinutes = set()
        for time in timePoints:
            minutes = convertToMinutes(time)
            maxMinutes = max(minutes, maxMinutes)
            if minutes in setMinutes:
                return 0
            setMinutes.add(minutes)

        # Iterate from max minutes to 0 to find the minimum difference
        previousMinutes = None
        minDifference = float("inf")
        for currentMinutes in range(maxMinutes, -1, -1):
            if currentMinutes in setMinutes:
                if previousMinutes is not None:
                    minDifference = min(minDifference, previousMinutes - currentMinutes)
                    minDifference = min(minDifference, (currentMinutes + 24 * 60) - previousMinutes)
                previousMinutes = currentMinutes

        # Final check
        minDifference = min(minDifference, maxMinutes - previousMinutes)
        minDifference = min(minDifference, (previousMinutes + 24 * 60) - maxMinutes)    

        return minDifference


S = Solution()
timePoints = ["23:59","00:00"]
print(S.findMinDifference(timePoints)) # 1
timePoints = ["00:00","23:59","00:00"]
print(S.findMinDifference(timePoints)) # 0
timePoints = ["00:00","04:00","22:00"]
print(S.findMinDifference(timePoints)) # 120