# 658 - https://leetcode.com/problems/find-k-closest-elements/

# Time: O(log(n - k) + k)
# Space: O(1)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # define pointers
        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left : left + k]
