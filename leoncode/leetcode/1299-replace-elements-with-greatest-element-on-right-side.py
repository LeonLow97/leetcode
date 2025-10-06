# 1299 - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Time: O(n) - We traverse the input array once.
# Space: O(n) 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Maintain a `rightMax` variable to keep track of the greatest element on the right side
        # Create a result array to store the greatest elements
        rightMax = -1
        result = [0] * len(arr)

        # Perform reversed for loop over `arr`
        for i in range(len(arr) - 1, -1, -1):
            # (i) Add to result array current rightMax at the current iteration index
            result[i] = rightMax

            # (ii) Check if current value is greater than rightMax, if yes, update rightMax
            if arr[i] > rightMax:
                rightMax = arr[i]

        return result
