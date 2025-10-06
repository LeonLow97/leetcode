# 153 - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Time: O(log n)
# Space: O(1)
class Solution:
    def findMin(self, arr: List[int]) -> int:
        if len(arr) == 1: return arr[0]

        left, right = 0, len(arr) - 1
        res = float("inf")

        while left <= right:
            middle = left + (right - left) // 2
            res = min(res, arr[middle])

            if arr[middle] > arr[right]:
                left = middle + 1
            else:
                right = middle - 1
        return res
