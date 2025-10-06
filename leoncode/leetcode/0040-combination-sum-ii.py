# 40 - https://leetcode.com/problems/combination-sum-ii/

# Time: O(2^n) in the worst case, where n is the number of candidates.
# Space: O(n) for the recursion stack and the subset list.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subset = [], []

        def dfs(i, curSum):
            if curSum == target:
                res.append(subset[:])
                return
            if curSum > target or i >= len(candidates):
                return

            # include the element
            subset.append(candidates[i])
            dfs(i+1, curSum + candidates[i])

            # exclude the element, skip duplicates
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curSum)
        
        dfs(0, 0)
        return res