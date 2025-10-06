# 78 - https://leetcode.com/problems/subsets/

# Time: O(2^n * n)
# Space: O(2^n * n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include the element
            subset.append(nums[i])
            dfs(i+1)

            # exclude the element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
