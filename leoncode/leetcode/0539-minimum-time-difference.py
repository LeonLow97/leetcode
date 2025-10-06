# 539 - https://leetcode.com/problems/minimum-time-difference/

# Time: O(N + 1440) where N is the number of time points
# Space: O(1440) because 1440 minutes in a day

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