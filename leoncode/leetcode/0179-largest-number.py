# 179 - https://leetcode.com/problems/largest-number/

# Time: O(n log n)
# Space: O(n)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsStr = [str(num) for num in nums]

        # custom comparator
        def compare(x, y):
            if (x + y) > (y + x):
                return -1
            else:
                return 1

        numsStr = sorted(numsStr, key=functools.cmp_to_key(compare))

        res = ''.join(numsStr)
        return "0" if res[0] == "0" else res