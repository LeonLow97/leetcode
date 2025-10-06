# 46 - https://leetcode.com/problems/permutations/

# Time: O(n * n!)
# Space: O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            temp = []
            for perm in res:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num)
                    temp.append(perm_copy)
            res = temp

        return res
