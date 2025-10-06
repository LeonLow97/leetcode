# 169 - https://leetcode.com/problems/majority-element/

# Time: O(n)
# Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n / 2
        hm = {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        for k, v in hm.items():
            if v > threshold:
                return k
        
        return -1
