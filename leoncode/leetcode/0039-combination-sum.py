# 39 - https://leetcode.com/problems/combination-sum/

# Time: O(2^n * n)
# Space: O(2^n * n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def dfs(i, curSum):
            if curSum == target:
                res.append(subset.copy())
                return 
            if curSum > target or i >= len(candidates):
                return

            # include the same number
            subset.append(candidates[i])
            dfs(i, curSum + candidates[i])

            # exclude the same number
            subset.pop()
            dfs(i+1, curSum)

        dfs(0, 0)
        return res
