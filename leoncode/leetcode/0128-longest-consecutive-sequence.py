# 128 - https://leetcode.com/problems/longest-consecutive-sequence/

# Time: O(n)
# Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        unique = set()
        for num in nums:
            unique.add(num)

        for num in unique:
            if (num-1) not in unique:
                # found start of sequence
                temp = 0
                while num in unique:
                    temp += 1
                    num += 1
                res = max(res, temp)
        
        return res