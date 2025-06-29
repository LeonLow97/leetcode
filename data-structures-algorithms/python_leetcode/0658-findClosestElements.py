'''
Difficulty: MEDIUM
No.658    https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return 
the k closest integers to x in the array. The result should also 
be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Constraints:
- 1 <= k <= arr.length
- 1 <= arr.length <= 10^4
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4
'''

# Questions to ask during interview:
# Is it always an increment of 1 between the elements? or there
# can be a case of [1,4,6,8,12]

from typing import List

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

s = Solution()
print(s.findClosestElements([1,2,3,4,5], 4, 3)) # [1,2,3,4]
print(s.findClosestElements([1,2,3,4,5],4,-1)) # [1,2,3,4]