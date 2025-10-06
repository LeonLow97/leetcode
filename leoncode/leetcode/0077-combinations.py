# 77 - https://leetcode.com/problems/combinations/

# Time: O(n * 2^n)
# Space: O(k * 2^n)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(num):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if num > n:
                return

            # include the number
            subset.append(num)
            backtrack(num + 1)

            # exclude the number
            subset.pop()
            backtrack(num + 1)

        backtrack(1)
        return res
