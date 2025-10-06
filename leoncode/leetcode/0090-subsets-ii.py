# 90 - https://leetcode.com/problems/subsets-ii/

# Time: O(N * 2^N) where N is the length of nums
# Space: O(N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include the number
            subset.append(nums[i])
            dfs(i+1)

            # exclude the number
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res
