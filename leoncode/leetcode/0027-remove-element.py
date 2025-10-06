# 27 - https://leetcode.com/problems/remove-element/

# Time: O(N)
# Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums) - 1

        while k <= n:
            if nums[k] == val:
                nums[k] = nums[n]
                n -= 1
            else:
                k += 1

        return k