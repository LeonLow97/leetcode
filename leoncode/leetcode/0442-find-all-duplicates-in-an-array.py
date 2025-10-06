# 442 - https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        # The numbers are in the range [1, n] so they are positive.
        # (i) When getting num, it could be negative, so we take abs(num)
        # (ii) In each iteration, mark the number in nums[num - 1] as negative.
        #   If in the next iterations, we access nums[num - 1] and its negative, we found a duplicate
        for num in nums:
            num = abs(num)

            if nums[num - 1] < 0:
                res.append(num)

            nums[num - 1] = -nums[num - 1]

        return res