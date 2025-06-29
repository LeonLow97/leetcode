'''
Difficulty: EASY
No.1089    https://leetcode.com/problems/duplicate-zeros/

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting 
the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the 
above modifications to the input array in place and do not return anything.
'''

from typing import List

# My Solution
# Runtime: 72 ms, Memory: 14.9 MB
# Time complexity: O(n^2), Space complexity: O(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        counter = 0
        n = len(arr)

        while counter < n:
            if arr[counter] == 0:
                arr.insert(counter, 0)
                counter += 2
                continue
            counter += 1
        
        while len(arr) > n:
            arr.pop()

        return arr

S = Solution()
arr = [1,0,2,3,0,4,5,0]
print(S.duplicateZeros(arr)) # [1,0,0,2,3,0,0,4]
arr = [0,4,1,0,0,8,0,0,3]
print(S.duplicateZeros(arr)) # [0,0,4,1,0,0,0,0,8]

# Eric's Solution (using a queue)
# Runtime: 69ms, Memory: 14.7 MB
# Time complexity: O(N), Space complexity: O(N)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        # number of duplications
        duplicated = 2

        queue = []
        n = len(arr)
        pointer = 0

        while pointer < n:
            if arr[pointer] == 0:
                for i in range(duplicated):
                    queue.append(0)
            else:
                queue.append(arr[pointer])
            
            first = queue.pop(0)
            arr[pointer] = first
            pointer += 1            

        return arr
        
S = Solution()
arr = [1,0,2,3,0,4,5,0]
print(S.duplicateZeros(arr)) # [1,0,0,2,3,0,0,4]
arr = [0,4,1,0,0,8,0,0,3]
print(S.duplicateZeros(arr)) # [0,0,4,1,0,0,0,0,8]



