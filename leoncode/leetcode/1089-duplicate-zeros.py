# 1089 - https://leetcode.com/problems/duplicate-zeros/

# Time: O(N^2)
# Space: O(N)

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